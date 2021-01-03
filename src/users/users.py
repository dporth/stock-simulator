from flask import Flask, request, Response, jsonify, abort, Blueprint

users_bp = Blueprint('blueprint', __name__)

@users_bp.route('/', methods=['GET', 'POST'])
def users():
    """
    GET   - returns all users
    POST  - creates a new user with the request body data
    """
    if request.method == 'GET':
        return "Returned list of users"
    elif request.method == 'POST':
        return "Created a user"
    else:
        return "Wrong request method"
