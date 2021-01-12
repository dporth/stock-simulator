from src.dao.state_dao import StateDAO
from datetime import datetime

def get_states():
    """Returns a list of all states from the state table"""
    state_dao = StateDAO()
    result = state_dao.get_states()
    return process_response(result)

def get_state_by_id(state_id):
    """Returns all states specified by the provided state id."""
    response = {}
    successful_response = {}
    error_response = {}
    state_dao = StateDAO()
    result = state_dao.get_state_by_id(state_id)
    if len(result.all()) != 0:
        return process_response(result)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

def process_response(query):
    """Takes a query and formats the attributes in the query. Returns the formatted attributes."""
    response = {}
    states = []
    for row in query:
        state = {}
        state['state_id'] = row.state_id
        state['state_name'] = row.state_name
        states.append(state)
    response['data'] = states
    response['timestamp'] = datetime.utcnow()
    return response
