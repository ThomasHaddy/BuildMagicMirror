#!/usr/bin/env python3

from os import system

def main():
   system('python3 /home/pi/BuildMagicMirror/scripts/install-mirror.py')
   system("/home/pi/BuildMagicMirror/scripts/service/start-mirror-service.sh")
   print("\n---------Starting Magic Mirror-----------\n")

if __name__ == "__main__":
   main()
