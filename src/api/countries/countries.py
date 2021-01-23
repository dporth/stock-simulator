from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

countries_bp = Blueprint('countries', __name__)

@countries_bp.route('/countries', methods=['GET'])
#@requires_auth
def countries():
    """
    GET   - returns all countries
    """
    
    if request.method == 'GET':
        response = get_countries()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200 

@countries_bp.route('/countries/<int:id>', methods=['GET'])
#@requires_auth
def get_country(id):
    """
    GET   - returns the countries with the country id
    """
    if request.method == 'GET':
        response = get_country_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
