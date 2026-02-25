#!/usr/bin/env sh

# this script is meant to be sourced, not executed directly. 
# or add the execution as an alias in your .zshrc or .bashrc, e.g:
# alias p10k-git-symbols='source /path/to/p10k-git-symbols.sh'
# Then you can simply run `p10k-git-symbols` in any terminal and it will print the markdown table.
# It will print a markdown table explaining the meaning of different symbols in Powerlevel10k's Git status segment. 
# The table is rendered using the glow CLI tool, which is a markdown renderer for the terminal. 
# If glow is not installed, the script will attempt to install it using Homebrew.


set -eu

# ------------------------------

VERBOSE=0

while getopts "v" opt; do
  case "$opt" in
    v) VERBOSE=1 ;;
    *) echo "Usage: $0 [-v]"; exit 1 ;;
  esac
done
shift $((OPTIND - 1))

# ------------------------------

DOC_URL="https://github.com/romkatv/powerlevel10k/blob/master/README.md#what-do-different-symbols-in-git-status-mean"
GLOW_URL="https://github.com/charmbracelet/glow"

# ------------------------------

# Ensure glow is installed (via Homebrew)
# This is needed to render the markdown table below. 
# If glow is not installed, we will attempt to install it using Homebrew. 
# If Homebrew is not available, we will print an error message and exit.
if ! command -v glow >/dev/null 2>&1; then
  echo "glow not found. Installing with Homebrew..."
  echo "GLOW URL: $GLOW_URL"
  if ! command -v brew >/dev/null 2>&1; then
    echo "Error: Homebrew (brew) is not installed. Install it first: https://brew.sh/"
    exit 1
  fi
  brew install glow
fi

# ------------------------------

# Render the markdown table
cat <<'MD' | glow -p
| Symbol | Meaning | Source |
|---|---|---|
| `feature` | current branch; replaced with `#tag` or `@commit` if not on a branch | `git status --ignore-submodules=dirty` |
| `master` | remote tracking branch; only shown if different from local branch | `git rev-parse --abbrev-ref --symbolic-full-name @{upstream}` |
| `wip` | the latest commit's summary contains "wip" or "WIP" | `git show --pretty=%s --no-patch HEAD` |
| `=` | up to date with the remote (neither ahead nor behind) | `git rev-list --count HEAD...@{upstream}` |
| `⇣42` | this many commits behind the remote | `git rev-list --right-only --count HEAD...@{upstream}` |
| `⇡42` | this many commits ahead of the remote | `git rev-list --left-only --count HEAD...@{upstream}` |
| `⇠42` | this many commits behind the push remote | `git rev-list --right-only --count HEAD...@{push}` |
| `⇢42` | this many commits ahead of the push remote | `git rev-list --left-only --count HEAD...@{push}` |
| `*42` | this many stashes | `git stash list` |
| `merge` | repository state | `git status --ignore-submodules=dirty` |
| `~42` | this many merge conflicts | `git status --ignore-submodules=dirty` |
| `+42` | this many staged changes | `git status --ignore-submodules=dirty` |
| `!42` | this many unstaged changes | `git status --ignore-submodules=dirty` |
| `?42` | this many untracked files | `git status --ignore-submodules=dirty` |
| `─` | the number of staged, unstaged or untracked files is unknown | `echo $POWERLEVEL9K_VCS_MAX_INDEX_SIZE_DIRTY` or `git config --get bash.showDirtyState` |
MD

# ------------------------------

if [ "$VERBOSE" -eq 1 ]; then
  # Print help text
  cat <<EOF
When using Lean, Classic or Rainbow style, Git status may look like this:
\`feature:master wip ⇣42⇡42 ⇠42⇢42 *42 merge ~42 +42 !42 ?42\`

To change the format of Git status, open ~/.p10k.zsh, search for my_git_formatter and edit its source code.
Documentation: $DOC_URL
EOF

fi




