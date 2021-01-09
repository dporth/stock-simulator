import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import User, Address, State, City, Country

class UserDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_users(self):
        """Returns all users with their address."""
        with self._db.session_scope() as session:
            return session.query(Address, User, State, City, Country).join(User).join(State).join(City).join(Country)
    
    def get_user_by_id(self, user_id):
        """Returns all users with their address that have the user id provided."""
        with self._db.session_scope() as session:
            return session.query(Address, User, State, City, Country).join(User).filter_by(user_id=user_id).join(State).join(City).join(Country)
    

    def delete_user(self, user_id):
        """Deletes all records in the user table that have the user id specified. Returns the user id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(User.user_id).filter_by(user_id=user_id)
            for row in results:
                marked_to_delete.append(row[0])
            user = session.query(User).filter_by(user_id=user_id).delete()
            session.flush()
            return marked_to_delete

    # todo return id
    def create_user(self, first_name, last_name, email, address_id):
        """Creates a record in the user table with the first name, last name, and address id specified. Returns the user id"""
        with self._db.session_scope() as session:
            user = User(first_name=first_name, last_name=last_name, email=email, address_id=address_id)
            session.add(user)
            session.flush()
            return user.user_id

if __name__ == "__main__":
    user = UserDAO()
    # Insert user functionality
    first_name = 'John'
    last_name = 'Doe'
    email = 'JohnDoe@gmail.com'
    address_id = 1

    id = user.create_user(first_name, last_name, email, address_id)
    print(id)
    # Get user functionality
    results = user.get_users()
    for row in results:
        print(row)

    # Delete user funcitonality
    print(user.delete_user(id))