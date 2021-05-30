import sys
import datetime
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import AccountValue
from sqlalchemy import and_

class AccountValueDAO():

    def get_account_value(self):
        """Returns all account_values."""
        return db_session.query(AccountValue)

    def delete_account_value(self, account_value_id):
        """Deletes all records in the account value table that have account value id specified. Returns the account value id of all records deleted."""
        marked_to_delete = []
        results = db_session.query(AccountValue.account_value_id).filter_by(account_value_id=account_value_id)
        for row in results:
            marked_to_delete.append(row[0])
        account_value = db_session.query(AccountValue).filter_by(account_value_id=account_value_id).delete()
        db_session.commit()
        return marked_to_delete

    def create_account_value(self, account_id, usd_account_amount):
        """Creates a record in the account value table with the parameters specified. Returns the account value id of the record created."""
        account_value = AccountValue(account_id=account_id, usd_account_amount=usd_account_amount)
        db_session.add(account_value)
        db_session.commit()
        return account_value.account_value_id

    def expire_account_value(self, account_id, usd_account_amount):
        """
            Expires the old account value specified by account id and creates a new record in the account value table with the other parameter specified. 
            Returns the account value id of the record created.
        """

        # Expire old record
        account_value = db_session.query(AccountValue).filter(and_(AccountValue.account_id==account_id, AccountValue.valid_to==None)).first()
        if account_value:
            account_value.valid_to = datetime.datetime.utcnow()
            db_session.commit()
        
        # Insert new record
        return self.create_account_value(account_id, usd_account_amount)

if __name__ == "__main__":
    account_value = AccountValueDAO()

    # Insert account_value functionality
    account_id = 2
    usd_account_amount = 503.162997


    id = account_value.create_account_value(account_id, usd_account_amount)
    print(id)
    # Get account_value functionality
    results = account_value.get_account_value()
    for row in results:
        print(row)

    # Delete account_value funcitonality
    print(account_value.delete_account_value(id))

    # Expire old record
    #usd_account_amount2 = 505.162997
    #id2 = account_value.expire_account_value(account_id, usd_account_amount2)
    #print(id2)

    # Get account_value functionality
    #results = account_value.get_account_value()
    #for row in results:
    #    print(row)