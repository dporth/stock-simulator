from src.dao.user_dao import UserDAO
from src.dao.state_dao import StateDAO
from src.dao.city_dao import CityDAO
from src.dao.country_dao import CountryDAO
from src.dao.address_dao import AddressDAO
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

    # Later used to determine if a new address needs to be created
    address_change = False

    user_dao = UserDAO()
    result = user_dao.get_user_by_id(user_id)
    if len(result.all()) != 0:
        # Check that only valid keys are passed
        user_keys = ['first_name', 'last_name', 'email']
        address_keys = ['street', 'postal_code', 'city', 'country', 'state']

        if len(json.keys()) > len(user_keys) + len(address_keys):
            error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
            error_response['code'] = '400'
            response['error'] = error_response
            response['timestamp'] = datetime.utcnow()
            return response

        for each in json.keys():
            if each not in user_keys and each not in address_keys:
                error_response['message'] = "Request body includes attributes that can not be updated. Invalid request."
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return response
            if each in address_keys:
                address_change = True
        
        # Validate user attributes

        # Update user address attributes if needed
        if address_change:
            if not required_keys(json, ['street', 'postal_code', 'city', 'country', 'state']):
                error_response['message'] = "Request body is missing required key value pairs. Invalid request."
                error_response['code'] = '400'
                response['error'] = error_response
                response['timestamp'] = datetime.utcnow()
                return response
            error_present, response = bad_address(json)
            if error_present:
                return response
            new_address_id = process_address(json)
            user_dao.update_user(user_id, 'address_id', new_address_id)

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
    city_dao = CityDAO()
    country_dao = CountryDAO()
    address_dao = AddressDAO()

    if not required_keys(json, ['first_name', 'last_name', 'email', 'street', 'postal_code', 'city', 'country', 'state']):
        error_response['message'] = "Request body is missing required key value pairs. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response
    error_present, response = bad_address(json)
    if error_present:
        return response
    
    new_address_id = process_address(json)
    first_name = json['first_name']
    last_name = json['last_name']
    email = json['email']

    # Create user
    new_user = user_dao.create_user(first_name, last_name, email, new_address_id)

    successful_response['user_id'] = new_user
    successful_response['first_name'] = first_name
    successful_response['last_name'] = last_name
    successful_response['email'] = email
    successful_response['address_id'] = new_address_id
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


def bad_address(json):
    """Returns True and the response if an error is present in the address.
    """
    response = {}
    successful_response = {}
    error_response = {}    

    state_dao = StateDAO()
    city_dao = CityDAO()
    country_dao = CountryDAO()
    address_dao = AddressDAO()
    
    street = json['street']
    postal_code = json['postal_code']
    city = json['city']
    country = json['country']
    state = json['state']

    # Get state, country, and city id
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

    result = city_dao.get_city(city).first()
    if result:
        city_id = result.city_id
    else:
        # city not found
        error_response['message'] = "Could not find city provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return True, response

    return False, {}

def process_address(json):
    """Takes in a json containing address key value pairs and creates the address 
    or finds the address id if the address already exists.
    """
    address_dao = AddressDAO()

    street = json['street']
    postal_code = json['postal_code']
    city = json['city']
    country = json['country']
    state = json['state']

    # Get address if it aleady exists
    result = address_dao.get_address(street, postal_code).first()
    if result:
        new_address_id = result.address_id
    else:
        # Create address
        new_address_id = address_dao.create_address(street, postal_code, country_id, state_id, city_id)
    return new_address_id

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
        user['address'] = {'street': row.Address.street, 'postal_code': row.Address.postal_code, 'city': row.City.city_name, 'state': row.State.state_name, 'country': row.Country.country_name}
        users.append(user)
    response['data'] = users
    response['timestamp'] = datetime.utcnow()
    return response