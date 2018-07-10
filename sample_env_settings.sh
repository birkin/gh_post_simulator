#!/bin/bash


## Settings instructions...
## - place this file somewhere out of the project path
## - edit the virtual-environment's `env/bin/activate` file by adding, at the bottom, the line:
##   `source "/path/to/this_settings_file.sh"` (no backticks)
## - update these settings
## - see the README for more info

export GH_SIM__LOG_PATH="/path/to/gh_simulator.log"

export GH_SIM__BASICAUTH_LISTENER_URL="http://username:password@127.0.0.1:8000/gh_listener/"

export GH_SIM__JSON_PAYLOAD='"foo"'
