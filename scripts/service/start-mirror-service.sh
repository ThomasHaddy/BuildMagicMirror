#!/bin/bash

SERV_PATH=/home/pi/BuildMagicMirror/scripts/service
$SERV_PATH/stop-mirror-service.sh
sudo cp $SERV_PATH/magic-mirror.service /etc/systemd/system/
sudo systemctl enable --now magic-mirror.service
echo "MagicMirror Service Created for Startup"

