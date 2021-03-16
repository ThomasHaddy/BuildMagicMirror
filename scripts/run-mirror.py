#!/usr/bin/env python3

import os
import subprocess
import shutil

def main():
   print()
   print("Starting Magic Mirror")
   print()
   os.chdir('/home/pi/MagicMirror/')
   if os.path.exists('/home/pi/config/config.js'):
      print("----------Using User Config--------------")
      shutil.copy2('/home/pi/config/config.js', '/home/pi/MagicMirror/config/')
   else:
      print("----------Using Sample Config------------")
      shutil.copy2('/home/pi/MagicMirror/config/config.js.sample', '/home/pi/MagicMirror/config/config.js')
   process = subprocess.Popen("npm run start".split(), stdout=subprocess.PIPE)
   output, error = process.communicate()

if __name__ == "__main__":
   main()

