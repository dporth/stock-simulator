from flask import Flask, request, Response, jsonify, abort, Blueprint
from .functions import *

api_bp = Blueprint('blueprint', __name__)

@api_bp.route('/users', methods=['GET', 'POST'])
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
    else:
        return jsonify("Wrong request method.")

@api_bp.route('/users/<int:user_id>', methods=['GET'])
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
    else:
        return jsonify("Wrong request method.")
