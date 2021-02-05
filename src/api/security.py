import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.config import api_auth0_audience, auth0_domain
from datetime import datetime

AUTH0_DOMAIN = auth0_domain
ALGORITHMS = ['RS256']
API_AUTH0_AUDIENCE = api_auth0_audience

def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get('Authorization', None)
    response = {}
    error_response = {}
    if not auth:
        error_response['message'] = 'Authorization header is expected. Authorization header missing.'
        error_response['code'] = '401'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
        error_response['message'] = 'Authorization header must start with "Bearer". Invalid request.'
        error_response['code'] = '401'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 401

    elif len(parts) == 1:
        error_response['message'] = 'Token not found. Invalid request.'
        error_response['code'] = '401'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 401

    elif len(parts) > 2:
        error_response['message'] = 'Authorization header must be bearer token. Invalid request.'
        error_response['code'] = '401'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 401

    token = parts[1]
    return token


def requires_auth(f):
    """Determines if the Access Token is valid. Creates a Python decorator.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
        jwks = json.loads(jsonurl.read())
        response = {}
        error_response = {}
        try:
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            for key in jwks['keys']:
                if key['kid'] == unverified_header['kid']:
                    rsa_key = {
                        'kty': key['kty'],
                        'kid': key['kid'],
                        'use': key['use'],
                        'n': key['n'],
                        'e': key['e']
                    }
        except Exception:
            error_response['message'] = 'Unable to parse authentication token. Invalid request.'
            error_response['code'] = '400'
            response['error'] = error_response
            response['timestamp'] = datetime.utcnow()
            return jsonify(response), 400


        user_id = ""

        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUTH0_AUDIENCE,
                    issuer='https://' + AUTH0_DOMAIN + '/'
                )
                
                # If bearer token is client credential set flag to later not allow post, delete, or put functionality
                if payload['gty'] == 'client-credentials':
                    user_id = "-1"
                else:
                    user_id = payload['sub']

                    # Validate user id
                    if '|' not in user_id:
                        error_response['message'] = "User id includes invalid characters. User must be a user registered with Auth0. Invalid request."
                        error_response['code'] = '400'
                        response['error'] = error_response
                        response['timestamp'] = datetime.utcnow()
                        return jsonify(response), 400
                    else:
                        user_id = user_id.split('|')[1]
                    
            except jwt.ExpiredSignatureError:
                error_response['message'] = 'Token expired.'
                error_response['code'] = '401'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return jsonify(response), 401
            except jwt.JWTClaimsError:
                error_response['message'] = 'Incorrect claims. Please, check the audience and issuer.'
                error_response['code'] = '401'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return jsonify(response), 401
            except Exception:
                error_response['message'] = 'Unable to parse authentication token. Invalid request.'
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return jsonify(response), 400

            _request_ctx_stack.top.current_user = payload
            return f(user_id, *args, **kwargs)

        error_response['message'] = 'Unable to find the appropriate key. Invalid request.'
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 400

    return decorated
    
def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return True
    return False
