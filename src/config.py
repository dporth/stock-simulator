import json

config = {}

with open('../config/dbconfig.json') as f:
    config = json.load(f)