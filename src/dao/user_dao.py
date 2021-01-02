import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import User

class UserDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_user(self):
        """Returns all users."""
        with self._db.session_scope() as session:
            return session.query(User)

    def delete_user(self, first_name, last_name):
        """Deletes all records in the user table that have the first and last name specified."""
        with self._db.session_scope() as session:
            session.query(User).filter_by(first_name=first_name, last_name=last_name).delete()
            session.flush()

    # todo return id
    def create_user(self, first_name, last_name, address_id):
        """Creates a record in the user table with the first name, last name, and address id specified. Returns the user id"""
        with self._db.session_scope() as session:
            user = User(first_name=first_name, last_name=last_name)
            session.add(user)
            session.flush()
            return user.user_id

if __name__ == "__main__":
    user = UserDAO()
    # Insert user functionality
    first_name = 'John'
    last_name = 'Doe'
    address_id = 1

    print(user.create_user(first_name, last_name, address_id))

    # Get user functionality
    results = user.get_user()
    for row in results:
        print(row)

    # Delete user funcitonality
    user.delete_user(first_name, last_name)