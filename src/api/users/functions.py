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


def create_user(json):
    response = {}
    successful_response = {}
    error_response = {}

    user_dao = UserDAO()
    state_dao = StateDAO()
    city_dao = CityDAO()
    country_dao = CountryDAO()
    address_dao = AddressDAO()

    first_name = json['first_name']
    last_name = json['last_name']
    email = json['email']
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
        return response

    result = country_dao.get_country(country).first()
    if result:
        country_id = result.country_id
    else:
        # country not found
        error_response['message'] = "Could not find country provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    result = city_dao.get_city(city).first()
    if result:
        city_id = result.city_id
    else:
        # city not found
        error_response['message'] = "Could not find city provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

   # Get address if it aleady exists
    result = address_dao.get_address(street, postal_code).first()
    if result:
        new_address_id = result.address_id
    else:
        # Create address
        new_address_id = address_dao.create_address(street, postal_code, country_id, state_id, city_id)

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