#!/bin/bash

# Add Google Chrome's official repository to the package manager
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# Update package list and install Google Chrome
sudo apt-get update
sudo apt-get install -y google-chrome-stable
