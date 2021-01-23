from flask import Flask, request, Response, jsonify, abort, Blueprint
from .functions import *
from src.api.security import requires_auth, requires_scope

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts', methods=['GET', 'POST'])
#@cross_origin(headers=["Content-Type", "Authorization"])
#@requires_auth
def accounts():
    """
    GET   - returns all accounts
    POST  - creates a new account with the request body data
    """
    
    if request.method == 'GET':
        response = get_accounts()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'POST':
        response = create_account(request.get_json())
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200

@accounts_bp.route('/accounts/<int:id>', methods=['GET', 'DELETE'])
#@requires_auth
def get_account(id):
    """
    GET    - returns the accounts with the account id
    DELETE - deletes the account specified by the account id
    """
    if request.method == 'GET':
        response = get_account_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'DELETE':
        response = delete_account(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200