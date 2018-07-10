# -*- coding: utf-8 -*-

""" Simulates a hit from github, for testing.
    (Turns out it's a GET, not a POST.)
    Assumes python3 env is activated. """

import json, logging, logging.config, os, pathlib, pprint, sys
import requests

# cwd = os.getcwd()  # so this assumes the cron call has cd-ed into the project directory
# if cwd not in sys.path:
#     print( 'adding ```%s``` to sys.path' % cwd  )
#     sys.path.append( cwd )


logging.basicConfig(
    filename=os.environ['GH_SIM__LOG_PATH'],
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
logging.propagte = False
log = logging.getLogger(__name__)
log.debug( 'logging ready' )


URL = os.environ[ 'GH_SIM__BASICAUTH_LISTENER_URL' ]  # example url: `http://username:password@127.0.0.1:8000/gh_listener/`
JSON_PAYLOAD = json.loads( os.environ['GH_SIM__JSON_PAYLOAD'] )  # can be as simple as '"foo"', or complex json


try:
    r = requests.get( URL, data=JSON_PAYLOAD )
    print( r.content )
except Exception as e:
    message = 'exception, ```%s```' % e
    log.error( message )
    print( message )
