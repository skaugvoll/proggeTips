#!/bin/bash
source ./install_homebrew.sh

# Check if homebrew is installed, else ask for install confirmation
hb=$(install_homebrew_fnc)
echo "HB: $hb"

exit
# Install terraform
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
brew update
brew upgrade hashicorp/tap/terraform

# Verify install
terraform -help
terraform -help plan

# Enable auto-complete
## ask if user have bash or zsh
### BASH

### ZSH
### store which shell is used (bash or zsh)
shell_rc_file="~/.zshrc"

## Install autocomplete
terraform -install-autocomplete

## Restart shell for autocomplete to be enabled
source $shell_rc_file

# Link to Quick Start for Terraform
echo "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#quick-start-tutorial"
