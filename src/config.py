import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Stock market API token from system environment variable
api_token = os.environ.get('MARKET_STACK_API_KEY')
polygon_queue_api_key = os.environ.get('POLYGON_QUEUE_API_KEY')
polygon_stock_price_updated_key = os.environ.get('POLYGON_STOCK_PRICE_UPDATER_KEY')

auth0_domain = os.environ.get('AUTH0_DOMAIN')
api_auth0_audience = os.environ.get('API_AUTH0_AUDIENCE')
auth0_mgt_client_secret = os.environ.get('AUTH0_MGT_CLIENT_SECRET')
auth0_mgt_client_id = os.environ.get('AUTH0_MGT_CLIENT_ID')
auth0_mgt_api_audience = os.environ.get('AUTH0_MGT_API_AUDIENCE')

# Stock market end of day api endpoint and
market_stack_eod_endpoint = 'http://api.marketstack.com/v1/eod/latest'
polygon_stock_eod_endpoint = "https://api.polygon.io/v2/aggs/ticker/{ticker:}/prev?unadjusted=true&apiKey={key:}"

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
mssql['database'] = os.environ.get('DATABASE_NAME')
mssql['schema'] = os.environ.get('DATABASE_SCHEMA')
config['mssql'] = mssql