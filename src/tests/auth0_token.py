import requests
from config import auth0_client_id, auth0_client_secret, auth0_audience, auth0_domain
import json

payload = {}
payload["client_id"] = auth0_client_id
payload["client_secret"] = auth0_client_secret
payload["audience"] = auth0_audience
payload["grant_type"] = "client_credentials"

payload = json.dumps(payload)

headers = { 'content-type': "application/json" }

response = requests.post(f"https://{auth0_domain}/oauth/token", data=payload, headers=headers)

print(response.text)