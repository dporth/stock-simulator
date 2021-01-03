import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Flask configuration
dotenv_path = join(dirname('./config/'), '.env')
load_dotenv(dotenv_path)

# Database configuration
config = {}

with open('./config/dbconfig.json') as f:
    config = json.load(f)