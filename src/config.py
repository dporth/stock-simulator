import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Stock market API token from system environment variable
api_token = os.environ.get('MARKET_STACK_API_KEY')
auth0_domain = os.environ.get('MARKET_STACK_API_KEY')
api_audience = os.environ.get('MARKET_STACK_API_KEY')

# Stock market end of day api endpoint
market_stack_eod_endpoint = 'http://api.marketstack.com/v1/eod/latest'

# Flask configuration
dotenv_path = join(dirname('./config/'), '.env')
load_dotenv(dotenv_path)

# Database configuration
config = {}
mssql = {}

mssql['user'] = os.environ.get('DATABASE_ACCOUNT')
mssql['server'] = os.environ.get('DATABASE_SERVER')
mssql['password'] = os.environ.get('DATABASE_PASSWORD')
mssql['port'] = '1433'
mssql['database'] = 'SIMS'
mssql['schema'] = 'stockmarket'
config['mssql'] = mssql