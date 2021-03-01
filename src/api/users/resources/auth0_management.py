from src.config import auth0_mgt_client_id, auth0_mgt_client_secret, auth0_mgt_api_audience, auth0_domain
import json
import requests

class Auth0Management():

    def get_token(self):
        payload = {}
        payload["client_id"] = auth0_mgt_client_id
        payload["client_secret"] = auth0_mgt_client_secret
        payload["audience"] = auth0_mgt_api_audience
        payload["grant_type"] = "client_credentials"
        payload["scope"] = "delete:users"

        payload = json.dumps(payload)

        headers = { 'content-type': "application/json" }

        response = requests.post(f"https://{auth0_domain}/oauth/token", data=payload, headers=headers)

        text = json.loads(response.text)

        return text['access_token']

    def delete_user(self, user_id):
        auth_type = "auth0"
        if '.' in user_id:
            auth_type = "apple"
        url = f"https://{auth0_domain}/api/v2/users/{auth_type}|{user_id}"

        payload={}
        headers = {
            'Authorization': f'Bearer {self.get_token()}',
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(response.status_code)
        return response.status_code
