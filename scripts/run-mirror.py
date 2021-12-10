#!/usr/bin/env python3

import os
import subprocess
from shutil import copy2

def get_config():
   if os.path.exists("/home/pi/config/config.js"):
      print("\n----------Using User Config--------------\n")
      copy2("/home/pi/config/config.js", "/home/pi/MagicMirror/config/")
   else:
      print("\n----------Using Sample Config------------\n")
      copy2("/home/pi/MagicMirror/config/config.js.sample", "/home/pi/MagicMirror/config/config.js")

def main():
   print()
   print("Starting Magic Mirror")
   get_config()
   os.chdir('/home/pi/MagicMirror/')
   process = subprocess.Popen("npm run start".split(), stdout=subprocess.PIPE)
   output, error = process.communicate()

if __name__ == "__main__":
   main()
