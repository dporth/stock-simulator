import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import User, Account, AccountValue
from sqlalchemy import and_


class UserDAO():

    def get_users(self):
        """Returns all users with their location."""
        return db_session.query(User)
    
    def get_user_by_id(self, user_id):
        """Returns all users with their location that have the user id provided."""
        return db_session.query(User).filter_by(user_id=user_id)
    
    def delete_user(self, user_id):
        """Deletes all records in the user table that have the user id specified. Returns the user id of the user deleted."""
        accounts = db_session.query(Account).filter(Account.user_id==user_id)
        for row in accounts:
            account_values_del = db_session.query(AccountValue).filter(AccountValue.account_id==row.account_id).delete()
            accounts_del = db_session.query(Account).filter(and_(Account.user_id==user_id, Account.account_id==row.account_id)).delete()
        users_del = db_session.query(User).filter_by(user_id=user_id).delete()
        db_session.commit()
        return user_id

    def update_user(self, user_id, key, value):
        """Updates the attribute specified by the key of a record for the user specified by the user id to the new value."""
        results = db_session.query(User).filter(User.user_id==user_id).update({key: value})
        db_session.commit()
        return user_id

    def get_user_by_identifier(self, identifier):
        """Returnes all users with the identifier specified."""
        return db_session.query(User).filter_by(identifier=identifier)
    
    def create_user(self, user_id, identifier):
        """Creates a record in the user table. Returns the user id"""
        user = User(user_id=user_id, identifier=identifier)
        db_session.add(user)
        db_session.commit()
        return user.user_id