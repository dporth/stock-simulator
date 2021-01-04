import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Address
from sqlalchemy import and_


class AddressDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_addresses(self):
        """Returns all addresses."""
        with self._db.session_scope() as session:
            return session.query(Address)
    
    def get_address(self, street, postal_code):
        """Returns all addresses that have the address street and postal code provided."""
        with self._db.session_scope() as session:
            return session.query(Address).filter(and_(Address.postal_code==postal_code, Address.street==street))
    
    def delete_address(self, address_id):
        """Deletes all records in the address table that have address id specified. Returns the address id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(Address.address_id).filter_by(address_id=address_id)
            for row in results:
                marked_to_delete.append(row[0])
            address = session.query(Address).filter_by(address_id=address_id).delete()
            session.flush()
            return marked_to_delete

    def create_address(self, street, postal_code, country_id, state_id, city_id):
        """Creates a record in the address table with the parameters specified. Returns the address id of the record created."""
        with self._db.session_scope() as session:
            address = Address(street=street, postal_code=postal_code, country_id=country_id, state_id=state_id, city_id=city_id)
            session.add(address)
            session.flush()
            return address.address_id

if __name__ == "__main__":
    address = AddressDAO()

    # Insert address functionality
    street = '6th way place'
    postal_code = '123456'
    country_id = '1'
    state_id = '1'
    city_id = '1'


    id = address.create_address(street, postal_code, country_id, state_id, city_id)
    print(id)
    # Get address functionality
    results = address.get_addresses()
    for row in results:
        print(row)

    # Delete address funcitonality
    print(address.delete_address(id))

    # Get a specific address
    results = address.get_address('1 Centre St, New York', '10007')
    for row in results:
        print(row)