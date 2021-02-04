from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET', 'POST'])
@requires_auth
def users(user_id):
    """
    GET   - returns all users
    POST  - creates a new user with the request body data
    """
    
    if request.method == 'GET':
        response = get_users()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'POST':
        if user_id == "-1":
            response = {}
            error_response = {}
            error_response['message'] = "Token provided cannot be used for this http request type. Invalid request."
            error_response['code'] = '400'
            response['error'] = error_response
            response['timestamp'] = datetime.utcnow()
            return jsonify(response), 400
        # Creates a user using user id from Bearer token provided
        response = create_user(request.get_json(), user_id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200

@users_bp.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
#@requires_auth
def get_user(id):
    """
    GET    - returns the users with the user id
    PUT    - updates the user attributes with the values in the request body
    DELETE - deletes the user specified by the user id
    """
    if request.method == 'GET':
        response = get_user_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'PUT':
        response = update_user(id, request.get_json())
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'DELETE':
        response = delete_user(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200