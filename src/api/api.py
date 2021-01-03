from flask import Blueprint

api_bp = Blueprint('blueprint', __name__)

@api_bp.route('/test')
def index():
    return "Hello World!"