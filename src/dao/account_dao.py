import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import Account, User, Stock, AccountValue, AccountValueQueueUpdated, StockPriceHistory
from sqlalchemy import and_, or_
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from src.dao.account_value_queue_updated_dao import AccountValueQueueUpdatedDAO

class AccountDAO():

    def get_accounts(self):
        """Returns all accounts with their users and stockss."""
        return db_session.query(Account, User, Stock, AccountValue).join(User).join(Stock).join(AccountValue, isouter=True).filter(AccountValue.valid_to == None)

    def get_accounts_to_refresh(self):
        """Returns all accounts that have an account value older than a day."""
        return db_session.query(Account, AccountValue, AccountValueQueueUpdated, StockPriceHistory).join(StockPriceHistory, StockPriceHistory.stock_id == Account.stock_id).join(AccountValue, Account.account_id == AccountValue.account_id, isouter=True).join(AccountValueQueueUpdated, AccountValue.account_value_id == AccountValueQueueUpdated.account_value_id, isouter=True).filter(and_(or_(AccountValue.valid_from < (datetime.now() + relativedelta(hours=-12)), AccountValueQueueUpdated.account_value_id != None, and_(StockPriceHistory.valid_from < (datetime.now() + relativedelta(hours=-2)), StockPriceHistory.valid_to == None)), AccountValue.valid_to == None))

    def get_account_values(self, account_id, records_since_date):
        """Returns account with its account value."""
        return db_session.query(Account, AccountValue).join(AccountValue).filter(and_(AccountValue.account_id==account_id, AccountValue.valid_from >= records_since_date))

    def get_accounts_by_user_id(self, user_id):
        """Returns all accounts belonging to the user id specified."""
        return db_session.query(Account, User, Stock, AccountValue).join(AccountValue, isouter=True).join(Stock).join(User).filter(User.user_id==user_id).order_by(Account.account_id.desc(), AccountValue.valid_from.asc())

    def get_accounts_by_stock(self, stock_id):
        """Returns all accounts that are for a specific stock id."""
        return db_session.query(Account).filter_by(stock_id=stock_id)       

    def get_account_by_id(self, account_id):
        """Returns all accounts with their address that have the account id provided."""
        return db_session.query(Account, AccountValue, User, Stock).join(AccountValue, isouter=True).filter(and_(Account.account_id==account_id)).join(User).join(Stock)
    
    def delete_account(self, account_id):
        """Deletes the account record and all account values belonging to the specified account it. 
        Returns the account id of all records deleted.
        """
        account_value_ids = []

        accounts = db_session.query(Account.account_id).filter_by(account_id=account_id)
        for row in accounts:
            account_value = db_session.query(AccountValue).filter(AccountValue.account_id==row.account_id)
            for row in account_value:
                account_value_ids.append(row.account_value_id)
            db_session.query(AccountValueQueueUpdated).filter(AccountValueQueueUpdated.account_value_id.in_(account_value_ids)).delete(synchronize_session=False)
            account_values_del = db_session.query(AccountValue).filter(AccountValue.account_id==row.account_id).delete()
        account = db_session.query(Account).filter_by(account_id=account_id).delete()
        db_session.commit()
        return account_id

    def create_account(self, share_price, share_amount, stock_id, user_id):
        """Creates a record in the account table with the parameters specified. Returns the account id of the record created."""        
        account = Account(share_price=share_price, share_amount=share_amount, stock_id=stock_id, user_id=user_id, create_date=(datetime.now() + relativedelta(hours=-12)))
        db_session.add(account)
        db_session.commit()
        return account.account_id