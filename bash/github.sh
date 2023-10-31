#!/bin/bash

# GitHub user information
github_username="YourUsername"
github_email="you@email.com"
github_fullname="FirstName LastName"
custom_ssh_key="customsshkey"

# Specify the output file path for the SSH key
ssh_key_output_file="$HOME/.ssh/$custom_ssh_key"

# Check if the ~/.ssh directory exists, and create it if it doesn't
if [ ! -d ~/.ssh ]; then
    mkdir ~/.ssh
fi

# Set local Git configuration
git config --local user.name "$github_fullname"
git config --local user.email "$github_email"

# Generate an SSH key and specify the output file
cd ~/.ssh
ssh-keygen -o -t rsa -b 4096 -C "$github_email" -f "$ssh_key_output_file"

# Add the SSH key to the SSH agent
ssh-add "$ssh_key_output_file"

# Check SSH login to GitHub
ssh -T git@github.com

# Check loaded keys
ssh-add -l