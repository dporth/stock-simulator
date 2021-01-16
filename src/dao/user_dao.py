import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import User, Location, State, Country, Account, AccountValue
from sqlalchemy import and_


class UserDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_users(self):
        """Returns all users with their location."""
        with self._db.session_scope() as session:
            return session.query(Location, User, State, Country).join(User).join(State).join(Country)
    
    def get_user_by_id(self, user_id):
        """Returns all users with their location that have the user id provided."""
        with self._db.session_scope() as session:
            return session.query(Location, User, State, Country).join(User).filter_by(user_id=user_id).join(State).join(Country)
    
    def delete_user(self, user_id):
        """Deletes all records in the user table that have the user id specified. Returns the user id of the user deleted."""
        with self._db.session_scope() as session:
            accounts = session.query(Account).filter(Account.user_id==user_id)
            for row in accounts:
                account_values_del = session.query(AccountValue).filter(AccountValue.account_id==row.account_id).delete()
                accounts_del = session.query(Account).filter(and_(Account.user_id==user_id, Account.account_id==row.account_id)).delete()
            users_del = session.query(User).filter_by(user_id=user_id).delete()
            session.flush()
            return user_id

    def update_user(self, user_id, key, value):
        """Updates the attribute specified by the key of a record for the user specified by the user id to the new value."""
        with self._db.session_scope() as session:
            results = session.query(User).filter(User.user_id==user_id).update({key: value})
            session.commit()
            return user_id

    def create_user(self, first_name, last_name, email, location_id):
        """Creates a record in the user table with the first name, last name, and location id specified. Returns the user id"""
        with self._db.session_scope() as session:
            user = User(first_name=first_name, last_name=last_name, email=email, location_id=location_id)
            session.add(user)
            session.flush()
            return user.user_id

if __name__ == "__main__":
    user = UserDAO()
    # Insert user functionality
    first_name = 'John'
    last_name = 'Doe'
    email = 'JohnDoe@gmail.com'
    location_id = 1

    id = user.create_user(first_name, last_name, email, location_id)
    print(id)
    # Get user functionality
    results = user.get_users()
    for row in results:
        print(row)

    # Delete user funcitonality
    print(user.delete_user(id))