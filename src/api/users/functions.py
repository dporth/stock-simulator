from src.dao.user_dao import UserDAO
from src.dao.state_dao import StateDAO
from src.dao.country_dao import CountryDAO
from src.dao.location_dao import LocationDAO
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

    # Later used to determine if a new location needs to be created
    location_change = False

    user_dao = UserDAO()
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        # Check that only valid keys are passed
        user_keys = ['first_name', 'last_name', 'email']
        location_keys = ['country', 'state']

        if len(json.keys()) > len(user_keys) + len(location_keys):
            error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
            error_response['code'] = '400'
            response['error'] = error_response
            response['timestamp'] = datetime.utcnow()
            return response

        for each in json.keys():
            if each not in user_keys and each not in location_keys:
                error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return response
            if each in location_keys:
                location_change = True
        
        # Validate user attributes
        if 'email' in json.keys():
            # Validate email
            email_error_present, email_response = bad_email(json['email'])
            if email_error_present:
                return email_response

        # Update user location attributes if needed
        if location_change:
            if not required_keys(json, location_keys):
                error_response['message'] = "Request body is missing required key value pairs. Invalid request."
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return response
            location_error_present, location_response = bad_location(json)
            if location_error_present:
                return location_response
            new_location_id = process_location(location_response)
            user_dao.update_user(user_id, 'location_id', new_location_id)

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


def create_user(json):
    """Creates a new user and returns the user attributes."""
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()
    state_dao = StateDAO()

    country_dao = CountryDAO()
    location_dao = LocationDAO()

    # Validate location
    if not required_keys(json, ['user_id', 'first_name', 'last_name', 'email', 'country', 'state']):
        error_response['message'] = "Request body is missing required key value pairs. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    if '|' in json['user_id']:
        error_response['message'] = "User id includes invalid characters. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    location_error_present, location_response = bad_location(json)
    if location_error_present:
        return location_response
    
    # Validate email
    email_error_present, email_response = bad_email(json['email'])
    if email_error_present:
        return email_response

    user_id = json['user_id']

    # Validate user id
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        error_response['message'] = "A resource already exists with that id. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    new_location_id = process_location(location_response)
    first_name = json['first_name']
    last_name = json['last_name']
    email = json['email']

    # Create user
    new_user = user_dao.create_user(user_id, first_name, last_name, email, new_location_id)

    successful_response['user_id'] = new_user
    successful_response['first_name'] = first_name
    successful_response['last_name'] = last_name
    successful_response['email'] = email
    successful_response['location_id'] = new_location_id
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


def bad_location(json):
    """Returns True and the response if an error is present in the location.
    """
    response = {}
    successful_response = {}
    error_response = {}    

    state_dao = StateDAO()
    country_dao = CountryDAO()
    location_dao = LocationDAO()
    
    country = json['country']
    state = json['state']

    # Get state, country
    result = state_dao.get_state(state).first()
    if result:
        state_id = result.state_id
    else:
        # state not found
        error_response['message'] = "Could not find state provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return True, response

    result = country_dao.get_country(country).first()
    if result:
        country_id = result.country_id
    else:
        # country not found
        error_response['message'] = "Could not find country provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return True, response

    return False, {'state_id': state_id, 'country_id': country_id}

def process_location(ids):
    """Takes in a json containing location ids. Creates the location or finds the location id if the location already exists.
    """
    location_dao = LocationDAO()

    # Get location if it aleady exists
    result = location_dao.get_location(ids['state_id'], ids['country_id']).first()
    if result:
        new_location_id = result.location_id
    else:
        # Create location
        new_location_id = location_dao.create_location(ids['state_id'], ids['country_id'])
    return new_location_id

def process_response(query):
    """Takes a query and formats the attributes in the query. Returns the formatted attributes."""
    response = {}
    users = []
    for row in query:
        user = {}
        user['user_id'] = row.User.user_id
        user['first_name'] = row.User.first_name
        user['last_name'] = row.User.last_name
        user['email'] = row.User.email
        user['location'] = {'state': row.State.state_name, 'country': row.Country.country_name}
        users.append(user)
    response['data'] = users
    response['timestamp'] = datetime.utcnow()
    return response

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
