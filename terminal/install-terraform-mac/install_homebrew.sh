#!/bin/sh

install_homebrew_fnc() {
	# Check if homebrew is installed, else ask for install confirmation
	is_installed=$(which brew)
	command_exit_code=$?
	echo "1: $is_installed -> $command_exit_code"
	if [[ -z "$is_installed" ]] || [ $command_exit_code -gt 0 ]; then
		echo "Brew is not installed"
		echo "Do you want to install it? [y/n]"
		read install_homebrew
		if [ "$install_homebrew" != "y"] || [ "$install_homebrew" != "n" ]; then
			# make this a recursive function, and call it again until user answers correctly
			echo "please type y or n"
			install_homebrew_fnc # call function again
		else
			if [ "$install_homebrew" == "y" ]; then
				# install homebrew
				echo "installing homebrew"
				return 0

			else
				echo "skipping installing homebrew"
				return 1
			fi
		fi

	else
		echo "brew is installed"
		return 0
	fi
}
