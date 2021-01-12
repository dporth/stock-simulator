from src.dao.city_dao import CityDAO
from datetime import datetime

def get_cities():
    """Returns a list of all cities from the city table"""
    city_dao = CityDAO()
    result = city_dao.get_cities()
    return process_response(result)

def get_city_by_id(city_id):
    """Returns all cities specified by the provided city id."""
    response = {}
    successful_response = {}
    error_response = {}
    city_dao = CityDAO()
    result = city_dao.get_city_by_id(city_id)
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
    cities = []
    for row in query:
        city = {}
        city['city_id'] = row.city_id
        city['city_name'] = row.city_name
        cities.append(city)
    response['data'] = cities
    response['timestamp'] = datetime.utcnow()
    return response
