from src.dao.user_dao import UserDAO
from datetime import datetime

def get_users():
    """Returns a list of all users from the user table"""
    response = {}

    user_dao = UserDAO()
    result = user_dao.get_users()
    return process_response(result)

def get_user_by_id(user_id):
    """Returns all users specified by the provided user id."""
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        return process_response(result)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

def delete_user(user_id):
    """Deletes a user and all accounts and account values that belong to the user"""
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        deleted_user = user_dao.delete_user(user_id)
        successful_response['user_id'] = user_id
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response
    response['data'] = successful_response
    response['timestamp'] = datetime.utcnow()
    return response

def update_user(user_id, json):
    """Updates the user that belongs to the specified user id. Only keys present in the json will bw updated in database.
    Returns the user's updated data.
    """
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        # Check that only valid keys are passed
        user_keys = ['email']

        if len(json.keys()) > len(user_keys):
            error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
            error_response['code'] = '400'
            response['error'] = error_response
            response['timestamp'] = datetime.utcnow()
            return response

        for each in json.keys():
            if each not in user_keys:
                error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return response
        
        # Validate user attributes
        if 'email' in json.keys():
            # Validate email
            email_error_present, email_response = bad_email(json['email'])
            if email_error_present:
                return email_response

        # Update user attributes
        for each in json.keys():
            if each in user_keys:
                result = user_dao.update_user(user_id, each, json[each])
        return get_user_by_id(user_id)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response


def create_user(json, user_id):
    """Creates a new user and returns the user attributes."""
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()

    if not required_keys(json, ['email']):
        error_response['message'] = "Request body is missing required key value pairs. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    # Validate email
    email_error_present, email_response = bad_email(json['email'])
    if email_error_present:
        return email_response

    # Validate user id
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        error_response['message'] = "A resource already exists with that id. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    email = json['email']

    # Create user
    new_user = user_dao.create_user(user_id, email)

    successful_response['user_id'] = new_user
    successful_response['email'] = email
    response['data'] = successful_response
    response['timestamp'] = datetime.utcnow()
    return response

def required_keys(json, required):
    """Takes in a list of required keys and checks to see if each key in the json is present in the array of required keys.
    Returns True if all keys required are present otherwise returns False.
    """
    keys_found = []
    for each in json.keys():
        if each in required:
            keys_found.append(each)
    return set(keys_found) == set(required)

def bad_email(email):
    """Takes in an email and validates it. This validation includes ensuring no one else has an account with that email.
    Returns True and a json containing information about the issue if there are issues with the email otherwise returns False.
    """
    response = {}
    error_response = {} 

    user_dao = UserDAO()
    result = user_dao.get_user_by_email(email).first()
    if result:
        # Email found
        error_response['message'] = "Email already exists. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return True, response
    else:
        return False, {}

def process_response(query):
    """Takes a query and formats the attributes in the query. Returns the formatted attributes."""
    response = {}
    users = []
    for row in query:
        user = {}
        user['user_id'] = row.user_id
        user['email'] = row.email
        users.append(user)
    response['data'] = users
    response['timestamp'] = datetime.utcnow()
    return response