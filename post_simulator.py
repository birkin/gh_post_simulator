# -*- coding: utf-8 -*-

""" Simulates a post from github, for testing.
    Assumes python3 env is activated. """

import json, logging, logging.config, os, pathlib, pprint, sys
import requests


URL = os.environ[ 'POST_SIMULATOR__BASICAUTH_LISTENER_URL' ]
PAYLOAD = os.environ[ 'POST_SIMULATOR__PAYLOAD' ]
LOG_CONFIG_DCT = os.environ[ 'POST_SIMULATOR__LOG_CONFIG_DCT' ]


log = logging.getLogger( 'gh_post_sim_logger' )
config_dct = json.loads( LOG_CONFIG_DCT )
logging.config.dictConfig( config_dct )
log.debug( 'logging ready' )



r = requests.get( URL )
print( r.content )

