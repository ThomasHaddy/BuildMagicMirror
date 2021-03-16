#!/usr/bin/env python3

import os
import subprocess
import shutil

# Installs using npm
def install():
   process = subprocess.Popen("npm install".split(), stdout=subprocess.PIPE)
   output, error = process.communicate()

# Installs a module using "module_name" as the directory
def install_module(module_name):
   print()
   print("Installing "+ module_name)
   os.chdir(os.path.expanduser("~")+'/MagicMirror/modules/' + module_name)
   install()

# Install
def main():
    install_module("MMM-NowPlayingOnSpotify")
    install_module("MMM-3Day-Forecast")
    os.chdir(os.path.expanduser("~")+'/MagicMirror/')
    shutil.copy2('/home/pi/config/config.js', '/home/pi/MagicMirror/config/')
    print()
    print("Installing Magic Mirror")
    install()
    os.system("python3 $HOME/MagicMirror/scripts/launch/run-mirror.py")

if __name__ == "__main__":
   main()

