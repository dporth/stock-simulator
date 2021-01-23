from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

states_bp = Blueprint('states', __name__)

@states_bp.route('/states', methods=['GET'])
#@requires_auth
def states():
    """
    GET   - returns all states
    """
    
    if request.method == 'GET':
        response = get_states()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200 

@states_bp.route('/states/<int:id>', methods=['GET'])
#@requires_auth
def get_state(id):
    """
    GET   - returns the states with the state id
    """
    if request.method == 'GET':
        response = get_state_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
