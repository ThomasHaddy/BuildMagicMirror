#!/bin/bash

sudo systemctl stop magic-mirror.service
sudo cp $HOME/MagicMirror/scripts/service-startup/magic-mirror.service /etc/systemd/system/
sudo systemctl enable --now magic-mirror.service
systemctl status magic-mirror.service
echo ""
echo "MagicMirror Service Created for Startup"

