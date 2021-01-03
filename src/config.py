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

with open('./config/dbconfig.json') as f:
    config = json.load(f)