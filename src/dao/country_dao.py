import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Country

class CountryDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_countries(self):
        """Returns all countrys."""
        with self._db.session_scope() as session:
            return session.query(Country)

    def get_country(self, country_name):
        """Returns all countries that have the country name provided."""
        with self._db.session_scope() as session:
            return session.query(Country).filter_by(country_name=country_name)

    def get_country_by_id(self, country_id):
        """Returns all countries that have the state id specified."""
        with self._db.session_scope() as session:
            return session.query(Country).filter_by(country_id=country_id)

    def delete_country(self, country_name):
        """Deletes all records in the country table that have the country_name specified. Returns the country id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(Country.country_id).filter_by(country_name=country_name)
            for row in results:
                marked_to_delete.append(row[0])
            country = session.query(Country).filter_by(country_name=country_name).delete()
            session.flush()
            return marked_to_delete

    # todo return country id
    def create_country(self, country_name):
        """Creates a record in the country table with the country_name specified. Returns the country id of the new record."""
        with self._db.session_scope() as session:
            country = Country(country_name=country_name)
            session.add(country)
            session.flush()
            return country.country_id

if __name__ == "__main__":
    country = CountryDAO()
    # Insert country functionality
    country_name = 'Italy'
    print(country.create_country(country_name))

    # Get country functionality
    results = country.get_countries()
    for row in results:
        print(row)

    # Delete country funcitonality
    print(country.delete_country(country_name))


    # Get a specific country
    results = country.get_country('United States')
    for row in results:
        print(row)