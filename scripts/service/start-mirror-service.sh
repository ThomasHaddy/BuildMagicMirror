#!/bin/bash

./stop-mirror-service.sh
sudo cp /home/pi/MagicMirror/scripts/service-startup/magic-mirror.service /etc/systemd/system/
sudo systemctl enable --now magic-mirror.service
echo "MagicMirror Service Created for Startup"
