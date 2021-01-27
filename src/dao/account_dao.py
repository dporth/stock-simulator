import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Account, User, Stock, AccountValue
from sqlalchemy import and_

class AccountDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_accounts(self):
        """Returns all accounts with their users and stockss."""
        with self._db.session_scope() as session:
            return session.query(Account, User, Stock, AccountValue).join(User).join(Stock).join(AccountValue, isouter=True).filter(AccountValue.valid_to == None)

    def get_account_values(self, account_id, records_since_date):
        """Returns all accounts with their users and stockss."""
        with self._db.session_scope() as session:
            return session.query(Account, AccountValue).join(AccountValue).filter(and_(AccountValue.account_id==account_id, AccountValue.valid_from >= records_since_date))



    def get_account_by_id(self, account_id):
        """Returns all accounts with their address that have the account id provided."""
        with self._db.session_scope() as session:
            return session.query(Account, AccountValue, User, Stock).filter_by(account_id=account_id).join(AccountValue).join(User).join(Stock)
    
    def delete_account(self, account_id):
        """Deletes the account record and all account values belonging to the specified account it. 
        Returns the account id of all records deleted.
        """
        with self._db.session_scope() as session:
            accounts = session.query(Account.account_id).filter_by(account_id=account_id)
            for row in accounts:
                account_values_del = session.query(AccountValue).filter(AccountValue.account_id==row.account_id).delete()
            account = session.query(Account).filter_by(account_id=account_id).delete()
            session.commit()
            return account_id

    def create_account(self, usd_amount, share_amount, stock_id, user_id):
        """Creates a record in the account table with the parameters specified. Returns the account id of the record created."""
        with self._db.session_scope() as session:
            account = Account(usd_amount=usd_amount, share_amount=share_amount, stock_id=stock_id, user_id=user_id)
            session.add(account)
            session.flush()
            return account.account_id

if __name__ == "__main__":
    account = AccountDAO()

    # Insert account functionality
    usd_amount = '341.73'
    share_amount = '1.463151'
    stock_id = '1'
    user_id = '4'


    id = account.create_account(usd_amount, share_amount, stock_id, user_id)
    print(id)
    # Get account functionality
    results = account.get_accounts()
    for row in results:
        print(row)

    # Delete account funcitonality
    print(account.delete_account(id))