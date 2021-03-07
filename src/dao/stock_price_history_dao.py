import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import StockPriceHistory
from sqlalchemy import and_


class StockPriceHistoryDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_stock_value(self, stock_id):
        """Returns the latest value for the given stock id."""
        with self._db.session_scope() as session:
            return session.query(StockPriceHistory).filter(and_(StockPriceHistory.stock_id==stock_id, StockPriceHistory.valid_to == None))
    
    def create_stock_value(self, stock_id, value):
        """Adds the specified stock id with the value to the stock price history table."""
        with self._db.session_scope() as session:
            stock_price_history = StockPriceHistory(stock_id=stock_id, historical_usd_price=value)
            session.add(stock_price_history)
            session.commit()
            return stock_price_history.stock_price_history_id
            
    def update_stock_value(self, stock_id, value):
        """Updates the value of the stock specified by the stock id in the stock history table."""
        with self._db.session_scope() as session:
            # Expire old record
            stock_history = session.query(StockPriceHistory).filter(and_(StockPriceHistory.stock_id==stock_id, StockPriceHistory.valid_to == None)).first()
            if stock_history :
                stock_history .valid_to = datetime.datetime.utcnow()
                session.commit()
        
        # Insert new record
        return self.create_account_value(account_id, usd_account_amount) 

            