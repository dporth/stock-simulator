import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Location
from sqlalchemy import and_


class LocationDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_locations(self):
        """Returns all locations."""
        with self._db.session_scope() as session:
            return session.query(Location)
    
    def get_location(self, state_id, country_id):
        """Returns all locations that have the location state and country provided."""
        with self._db.session_scope() as session:
            return session.query(Location).filter(and_(Location.state_id==state_id, Location.country_id==country_id))
    
    def delete_location(self, location_id):
        """Deletes all records in the location table that have location id specified. Returns the location id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(Location.location_id).filter_by(location_id=location_id)
            for row in results:
                marked_to_delete.append(row[0])
            location = session.query(Location).filter_by(location_id=location_id).delete()
            session.flush()
            return marked_to_delete

    def create_location(self, state_id, country_id):
        """Creates a record in the location table with the parameters specified. Returns the location id of the record created."""
        with self._db.session_scope() as session:
            location = Location(country_id=country_id, state_id=state_id)
            session.add(location)
            session.flush()
            return location.location_id

if __name__ == "__main__":
    location = LocationDAO()

    # Insert location functionality
    street = '6th way place'
    postal_code = '123456'
    country_id = '1'
    state_id = '1'
    city_id = '1'


    id = location.create_location(street, postal_code, country_id, state_id, city_id)
    print(id)
    # Get location functionality
    results = location.get_locations()
    for row in results:
        print(row)

    # Delete location funcitonality
    print(location.delete_location(id))

    # Get a specific location
    results = location.get_location('1 Centre St, New York', '10007')
    for row in results:
        print(row)