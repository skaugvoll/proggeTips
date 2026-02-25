#!/bin/sh

# The best use case for this script is to add it as a alias in e.g your .zshrc or .bashrc:
# alias ghopen='source /path/to/gh-repo-open.sh && openrepo'
# Then you can simply run `ghopen` in any git repository and it will open the repository in your default browser.

function openrepo() {
  # Ensure we're inside a git repo
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "Not a git repository."
    return 1
  fi

  # Get remote URL
  local remote_url
  remote_url=$(git remote get-url origin 2>/dev/null)
  if [[ -z "$remote_url" ]]; then
    echo "No remote origin found."
    return 1
  fi

  # Convert SSH or HTTPS to browser URL
  local web_url
  if [[ "$remote_url" == git@* ]]; then
    web_url="https://${remote_url#git@}"
    web_url="${web_url/:/\/}"
    web_url="${web_url%.git}"
  elif [[ "$remote_url" == http* ]]; then
    web_url="${remote_url%.git}"
  else
    echo "Unknown remote format: $remote_url"
    return 1
  fi

  # Current branch
  local branch
  branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "")
  if [[ -n "$branch" ]]; then
    # Try to find a pull request for this branch
    if command -v gh >/dev/null 2>&1; then
      # Use GitHub CLI if available
      local pr_url
      pr_url=$(gh pr view "$branch" --json url -q .url 2>/dev/null)
      if [[ -n "$pr_url" ]]; then
        echo "Opening pull request for branch '$branch'..."
        open "$pr_url"
        return 0
      fi
    fi
  fi

  echo "Opening repository root..."
  open "$web_url"
}

