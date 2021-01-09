from flask import Flask, request, Response, jsonify, abort, Blueprint
from .functions import *

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET', 'POST'])
@requires_auth
def users():
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
        response = create_user(request.get_json())
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200

@users_bp.route('/users/<int:user_id>', methods=['GET'])
@requires_auth
def get_user(user_id):
    """
    GET   - returns the users with the user id
    """
    if request.method == 'GET':
        response = get_user_by_id(user_id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200