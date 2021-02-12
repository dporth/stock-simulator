from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET', 'POST'])
@requires_auth
def users(user_id):
    """
    GET   - returns all users if authorization is done using client credentials, otherwise return user associated with bearer token
    POST  - creates a new user with the request body data if authorization is not done using client credentials
    """
    
    if request.method == 'GET':
        # allow all users to be returned if authorization is using client credentials
        if user_id == "-1":
            response = get_users()
        else: # return only the user attached to bearer token
            response = get_user_by_id(user_id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
    elif request.method == 'POST':
        if user_id == "-1":
            response = {}
            error_response = {}
            error_response['message'] = "Token provided cannot be used for this HTTP request method. Invalid request."
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
def get_user(user_id, id):
    """
    GET    - returns the users with the id
    PUT    - updates the user attributes with the values in the request body for the user that matches the id
    DELETE - deletes the user specified by the id
    """
    # do not allow request if user id associated with bearer token does not match resource
    if user_id != id:
        response = {}
        error_response = {}
        error_response['message'] = "Not authorized for the requested resource. Unauthorized."
        error_response['code'] = '401'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return jsonify(response), 401
    else:
        if request.method == 'GET':
            response = get_user_by_id(user_id)
            if 'error' in response:
                return jsonify(response), response['error']['code']
            else:
                return jsonify(response), 200
        elif request.method == 'PUT':
            response = update_user(user_id, request.get_json())
            if 'error' in response:
                return jsonify(response), response['error']['code']
            else:
                return jsonify(response), 200
        elif request.method == 'DELETE':
            response = delete_user(user_id)
            if 'error' in response:
                return jsonify(response), response['error']['code']
            else:
                return jsonify(response), 200