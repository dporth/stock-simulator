import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Address


class AddressDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_address(self):
        """Returns all addresss."""
        with self._db.session_scope() as session:
            return session.query(Address)

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
    results = address.get_address()
    for row in results:
        print(row)

    # Delete address funcitonality
    print(address.delete_address(id))