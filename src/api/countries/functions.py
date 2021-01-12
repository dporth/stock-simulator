from src.dao.country_dao import CountryDAO
from datetime import datetime

def get_countries():
    """Returns a list of all countries from the country table"""
    country_dao = CountryDAO()
    result = country_dao.get_countries()
    return process_response(result)

def get_country_by_id(country_id):
    """Returns all countries specified by the provided country id."""
    response = {}
    successful_response = {}
    error_response = {}
    country_dao = CountryDAO()
    result = country_dao.get_country_by_id(country_id)
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
    countries = []
    for row in query:
        country = {}
        country['country_id'] = row.country_id
        country['country_name'] = row.country_name
        countries.append(country)
    response['data'] = countries
    response['timestamp'] = datetime.utcnow()
    return response
