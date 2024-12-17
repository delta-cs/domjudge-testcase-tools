#!/bin/bash

# ensure python dependencies are installed
pip3 install -r requirements.txt



TARGET_DIR="$HOME/.local/bin"

SRC_PATH="./src/testcase-tools.py"

NAME="testcase-tools"

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Copy script to the target directory
cp "$SRC_PATH" "$TARGET_DIR/$NAME"

# Ensure the script is executable
chmod +x "$TARGET_DIR/$NAME"


printf "\n\033[1;32mInstallation complete!\033[0m\n"
echo "Make sure $TARGET_DIR is in your PATH."
echo "If it's not, add following to your .bashrc/.zshrc:"
printf "\033[3mexport PATH=\"$TARGET_DIR:\$PATH\"\033[0m\n"