#!/usr/bin/env python3

import os
import subprocess
from sys import exit
from shutil import copy2

# Installs using npm
def install():
   process = subprocess.Popen("npm install".split(), stdout=subprocess.PIPE)
   output, error = process.communicate()

# Installs a module using "module_name" as the directory
def install_module(module_name):
   print("\nInstalling "+ module_name)
   os.chdir("/home/pi/MagicMirror/modules/" + module_name)
   install()

# Installs the base application MagicMirror
def install_mirror():
   os.chdir("/home/pi/MagicMirror/")
   print("\nInstalling Magic Mirror")
   install()

def main():
   module_list = [ module for module in os.listdir("/home/pi/MagicMirror/modules/") if os.path.isdir(os.path.join("/home/pi/MagicMirror/modules/", module)) ]
   module_list.remove("default")
   print("Modules:\n" + ' \n'.join(module_list))
   for mod in module_list:
      install_module(mod)
   install_mirror()

if __name__ == "__main__":
   main()
