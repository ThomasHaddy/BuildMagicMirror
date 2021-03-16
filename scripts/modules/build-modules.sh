#!/bin/bash

# NOTE:
# This assumes you have set up ssh and have the modules and application
# on your peronal repositories
GIT="git@github.com:ThomasHaddy"

# Builds a module
function build_module
{
   echo ""
   echo "Building $1"
   if [ ! -d $HOME/MagicMirror/modules/$1 ]; then
      cd $HOME/MagicMirror/modules/
      git clone $GIT/$1.git
   cd $HOME/MagicMirror/modules/$1
   npm install
}

mkdir -p $HOME/git-local/MagicMirror

build_module "MMM-NowPlayingOnSpotify"
build_module "MMM-3Day-Forecast"
