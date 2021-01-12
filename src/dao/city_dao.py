import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import City

class CityDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_cities(self):
        """Returns all cities."""
        with self._db.session_scope() as session:
            return session.query(City)

    def get_city(self, city_name):
        """Returns all cities that have the city name provided."""
        with self._db.session_scope() as session:
            return session.query(City).filter_by(city_name=city_name)

    def get_city_by_id(self, city_id):
        """Returns all cities that have the city id specified."""
        with self._db.session_scope() as session:
            return session.query(City).filter_by(city_id=city_id)

    def delete_city(self, city_name):
        """Deletes all records in the city table that have the city_name specified. Returns the city id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(City.city_id).filter_by(city_name=city_name)
            for row in results:
                marked_to_delete.append(row[0])
            city = session.query(City).filter_by(city_name=city_name).delete()
            session.flush()
            return marked_to_delete

    # todo return city id
    def create_city(self, city_name):
        """Creates a record in the city table with the city_name specified. Returns the city id of the new record."""
        with self._db.session_scope() as session:
            city = City(city_name=city_name)
            session.add(city)
            session.flush()
            return city.city_id

if __name__ == "__main__":
    city = CityDAO()
    # Insert city functionality
    city_name = 'Louisville'
    print(city.create_city(city_name))

    # Get city functionality
    results = city.get_cities()
    for row in results:
        print(row)

    # Delete city funcitonality
    print(city.delete_city(city_name))

    # Get a specific city
    results = city.get_city('New York')
    for row in results:
        print(row)