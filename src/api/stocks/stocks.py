from flask import Flask, request, Response, jsonify, abort, Blueprint
from src.api.security import requires_auth, requires_scope
from .functions import *

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/stocks', methods=['GET'])
#@requires_auth
def stocks():
    """
    GET   - returns all stocks
    """
    
    if request.method == 'GET':
        response = get_stocks()
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200 

@stocks_bp.route('/stocks/<int:id>', methods=['GET'])
#@requires_auth
def get_stock(id):
    """
    GET   - returns the stocks with the stock id
    """
    if request.method == 'GET':
        response = get_stock_by_id(id)
        if 'error' in response:
            return jsonify(response), response['error']['code']
        else:
            return jsonify(response), 200
