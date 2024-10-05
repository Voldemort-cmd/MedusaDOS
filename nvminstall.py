#!/usr/bin/env python3

import os
import sys

# Update and install required packages for Kali Linux
os.system('sudo apt update -y && sudo apt install wget curl -y')

# Download and run the Debian installation script from Andronix (if you still need it)
os.system('wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh -O debian.sh && chmod +x debian.sh && bash debian.sh')

# Install npm (node package manager)
os.system('sudo apt install npm -y')

# Install nvm (Node Version Manager)
os.system('curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash')

# Reload bash configuration to make nvm available
os.system('source ~/.bashrc')

# Install the LTS version of Node.js using nvm
os.system('nvm install --lts')

# Reload bash configuration again to apply nvm changes
os.system('source ~/.bashrc')

# Success message
print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m]\x1b[0m \x1b[32m> \x1b[33mInstallation Successful")
