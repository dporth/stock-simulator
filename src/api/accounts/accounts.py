from flask import Flask, request, Response, jsonify, abort, Blueprint
from .functions import *
from src.api.security import requires_auth, requires_scope

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts', methods=['GET', 'POST'])
#@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def accounts(user_id):
    """
    GET   - returns all accounts
    POST  - creates a new account with the request body data
    """
    
    if request.method == 'GET':
        # allow return of all accounts for all users  if authorization is using client credentials
        if user_id == "-1":
            response = get_accounts()
        else: # return only the accounts attached to bearer token
            filter_requested = request.args.get('filters')
            if filter_requested == None:
                filters = {}
            else:
                filters = {"filters": filter_requested}
            response = get_accounts_by_user_id(str(user_id))
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'POST':
        response = create_account(user_id, request.get_json())
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200

@accounts_bp.route('/accounts/<int:id>', methods=['GET', 'DELETE'])
@requires_auth
def get_account(user_id, id):
    """
    GET    - returns the accounts with the account id
    DELETE - deletes the account specified by the account id
    """
    if request.method == 'GET':
        filter_requested = request.args.get('filters')
        if filter_requested == None:
            filters = {}
        else:
            filters = {"filters": filter_requested}
        response = get_account_by_id(id, filters)
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