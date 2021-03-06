import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import User, Account, AccountValue
from sqlalchemy import and_


class UserDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_users(self):
        """Returns all users with their location."""
        with self._db.session_scope() as session:
            return session.query(User)
    
    def get_user_by_id(self, user_id):
        """Returns all users with their location that have the user id provided."""
        with self._db.session_scope() as session:
            return session.query(User).filter_by(user_id=user_id)
    
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

    def get_user_by_identifier(self, identifier):
        """Returnes all users with the identifier specified."""
        with self._db.session_scope() as session:
            return session.query(User).filter_by(identifier=identifier)
    
    def create_user(self, user_id, identifier):
        """Creates a record in the user table. Returns the user id"""
        with self._db.session_scope() as session:
            user = User(user_id=user_id, identifier=identifier)
            session.add(user)
            session.flush()
            return user.user_id