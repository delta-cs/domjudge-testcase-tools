#!/bin/bash

TARGET_DIR="$HOME/.local/bin"

SRC_PATH="./src/testcase-tools.py"

NAME="testcase-tools"

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Copy script to the target directory
cp "$SRC_PATH" "$TARGET_DIR/$NAME"

# Ensure the script is executable
chmod +x "$TARGET_DIR/$NAME"

echo "Installation complete! Make sure $TARGET_DIR is in your PATH."
echo "If it's not, add following to your .bashrc/.zshrc:"
echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""