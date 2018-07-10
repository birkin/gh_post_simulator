#!/bin/bash


## Place this file somewhere out of the project path,
## ...update these settings, and call it via `../env/bin/activate`.
## See the README for more info.

export GH_SIM__LOG_PATH="/path/to/gh_simulator.log"

export GH_SIM__BASICAUTH_LISTENER_URL="http://username:password@127.0.0.1:8000/gh_listener/"

export GH_SIM__JSON_PAYLOAD='"foo"'
