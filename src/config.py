import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Stock market API token from system environment variable
api_token = os.environ.get('MARKET_STACK_API_KEY')
# Stock market end of day api endpoint
market_stack_eod_endpoint = 'http://api.marketstack.com/v1/eod/latest'

# Flask configuration
dotenv_path = join(dirname('./config/'), '.env')
load_dotenv(dotenv_path)

# Database configuration
config = {}
config['account'] = os.environ.get('DATABASE_ACCOUNT')
config['server'] = os.environ.get('DATABASE_SERVER')
config['password'] = os.environ.get('DATABASE_PASSWORD')
config['port'] = '1433'
config['database'] = 'SIMS'
config['schema'] = 'stockmarket'