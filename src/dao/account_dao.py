import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Account, User, Stock, AccountValue, AccountValueQueueUpdated, StockPriceHistory
from sqlalchemy import and_, or_
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from src.dao.account_value_queue_updated_dao import AccountValueQueueUpdatedDAO

class AccountDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_accounts(self):
        """Returns all accounts with their users and stockss."""
        with self._db.session_scope() as session:
            return session.query(Account, User, Stock, AccountValue).join(User).join(Stock).join(AccountValue, isouter=True).filter(AccountValue.valid_to == None)

    def get_accounts_to_refresh(self):
        """Returns all accounts that have an account value older than a day."""
        with self._db.session_scope() as session:
            return session.query(Account, AccountValue, AccountValueQueueUpdated, StockPriceHistory).join(StockPriceHistory, StockPriceHistory.stock_id == Account.stock_id).join(AccountValue, Account.account_id == AccountValue.account_id, isouter=True).join(AccountValueQueueUpdated, AccountValue.account_value_id == AccountValueQueueUpdated.account_value_id, isouter=True).filter(and_(or_(AccountValue.valid_from < (datetime.now() + relativedelta(hours=-12)), AccountValueQueueUpdated.account_value_id != None, and_(StockPriceHistory.valid_from < (datetime.now() + relativedelta(hours=-2)), StockPriceHistory.valid_to == None)), AccountValue.valid_to == None))

    def get_account_values(self, account_id, records_since_date):
        """Returns account with its account value."""
        with self._db.session_scope() as session:
            return session.query(Account, AccountValue).join(AccountValue).filter(and_(AccountValue.account_id==account_id, AccountValue.valid_from >= records_since_date))

    def get_accounts_by_user_id(self, user_id):
        """Returns all accounts belonging to the user id specified."""
        with self._db.session_scope() as session:
            return session.query(Account, User, Stock, AccountValue).join(AccountValue, isouter=True).join(Stock).join(User).filter(User.user_id==user_id).order_by(Account.account_id.desc(), AccountValue.valid_to.desc())

    def get_accounts_by_stock(self, stock_id):
        """Returns all accounts that are for a specific stock id."""
        with self._db.session_scope() as session:
            return session.query(Account).filter_by(stock_id=stock_id)       

    def get_account_by_id(self, account_id):
        """Returns all accounts with their address that have the account id provided."""
        with self._db.session_scope() as session:
            return session.query(Account, AccountValue, User, Stock).join(AccountValue, isouter=True).filter(and_(Account.account_id==account_id)).join(User).join(Stock)
    
    def delete_account(self, account_id):
        """Deletes the account record and all account values belonging to the specified account it. 
        Returns the account id of all records deleted.
        """
        account_value_ids = []
        with self._db.session_scope() as session:
            accounts = session.query(Account.account_id).filter_by(account_id=account_id)
            for row in accounts:
                account_value = session.query(AccountValue).filter(AccountValue.account_id==row.account_id)
                for row in account_value:
                    account_value_ids.append(row.account_value_id)
                session.query(AccountValueQueueUpdated).filter(AccountValueQueueUpdated.account_value_id.in_(account_value_ids)).delete(synchronize_session=False)
                account_values_del = session.query(AccountValue).filter(AccountValue.account_id==row.account_id).delete()
            account = session.query(Account).filter_by(account_id=account_id).delete()
            session.commit()
            return account_id

    def create_account(self, usd_amount, share_amount, stock_id, user_id):
        """Creates a record in the account table with the parameters specified. Returns the account id of the record created."""        
        with self._db.session_scope() as session:
            account = Account(usd_amount=usd_amount, share_amount=share_amount, stock_id=stock_id, user_id=user_id, create_date=(datetime.now() + relativedelta(hours=-12)))
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