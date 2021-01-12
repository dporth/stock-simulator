from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

cities_bp = Blueprint('cities', __name__)

@cities_bp.route('/cities', methods=['GET'])
@requires_auth
def cities():
    """
    GET   - returns all cities
    """
    
    if request.method == 'GET':
        response = get_cities()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200 

@cities_bp.route('/cities/<int:id>', methods=['GET'])
@requires_auth
def get_city(id):
    """
    GET   - returns the cities with the city id
    """
    if request.method == 'GET':
        response = get_city_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
