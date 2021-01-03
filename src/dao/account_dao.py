import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Account


class AccountDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_account(self):
        """Returns all accounts."""
        with self._db.session_scope() as session:
            return session.query(Account)

    def delete_account(self, account_id):
        """Deletes all records in the account table that have account id specified. Returns the account id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(Account.account_id).filter_by(account_id=account_id)
            for row in results:
                marked_to_delete.append(row[0])
            account = session.query(Account).filter_by(account_id=account_id).delete()
            session.flush()
            return marked_to_delete

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
    user_id = '1'


    id = account.create_account(usd_amount, share_amount, stock_id, user_id)
    print(id)
    # Get account functionality
    results = account.get_account()
    for row in results:
        print(row)

    # Delete account funcitonality
    print(account.delete_account(id))