# -*- coding: utf-8 -*-

""" Simulates a post from github, for testing.
    Assumes python3 env is activated. """

import json, logging, logging.config, os, pathlib, pprint, sys

cwd = os.getcwd()  # so this assumes the cron call has cd-ed into the project directory
if cwd not in sys.path:
    print( 'adding ```%s``` to sys.path' % cwd  )
    sys.path.append( cwd )

import requests


URL = os.environ[ 'GH_SIM__BASICAUTH_LISTENER_URL' ]
PAYLOAD = os.environ[ 'GH_SIM__PAYLOAD' ]
LOG_CONFIG_DCT = os.environ[ 'GH_SIM__LOG_CONFIG_DCT' ]


log = logging.getLogger( 'gh_post_sim_logger' )
config_dct = json.loads( LOG_CONFIG_DCT )
logging.config.dictConfig( config_dct )
log.debug( 'logging ready' )



r = requests.get( URL )
print( r.content )

