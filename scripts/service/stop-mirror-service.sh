#!/bin/bash

status="sudo systemctl status magic-mirror.service"
if [ eval $status -eq 0 ]; then
   sudo systemctl stop magic-mirror.service
fi
