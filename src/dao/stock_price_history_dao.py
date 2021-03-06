import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import StockPriceHistory
from sqlalchemy import and_
from datetime import datetime
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta

class StockPriceHistoryDAO():

    def get_stock_value(self, stock_id):
        """Returns the latest value for the given stock id."""
        return db_session.query(StockPriceHistory).filter(and_(StockPriceHistory.stock_id==stock_id, StockPriceHistory.valid_from >= (datetime.now() + relativedelta(days=-1)), StockPriceHistory.valid_to == None))
    
    def create_stock_value(self, stock_id, value):
        """Adds the specified stock id with the value to the stock price history table."""
        stock_price_history = StockPriceHistory(stock_id=stock_id, historical_usd_price=value)
        db_session.add(stock_price_history)
        db_session.commit()
        return stock_price_history.stock_price_history_id
            
    def update_stock_value(self, stock_id, value):
        """Updates the value of the stock specified by the stock id in the stock history table."""
        # Expire old record
        stock_history = db_session.query(StockPriceHistory).filter(and_(StockPriceHistory.stock_id==stock_id, StockPriceHistory.valid_to == None)).first()
        if stock_history:
            stock_history.valid_to = datetime.utcnow()
            db_session.commit()
    
        # Insert new record
        return self.create_stock_value(stock_id, value) 

            