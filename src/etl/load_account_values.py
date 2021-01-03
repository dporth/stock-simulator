import sys
[sys.path.append(i) for i in ['.', '..','../']]
import requests
from time import strftime
import json
import pandas as pd
from decimal import Decimal
from src.db.db_helper import DBHelper
from src.db.models import Stock, Account
from src.config import api_token, market_stack_eod_endpoint
from src.dao.stock_dao import StockDAO
from src.dao.account_value_dao import AccountValueDAO

class LoadAccountValues():
    def __init__(self):
        self._stock_dao = StockDAO()
        self._account_value_dao = AccountValueDAO()
        self._db = DBHelper()

    def get_account_stocks(self):
        """Returns all account and stock records where the account has a match to a stock id in the stock table."""
        with self._db.session_scope() as session:
            return session.query(Account, Stock).join(Stock)

    def get_stocks(self):
        return self._stock_dao.get_stocks()

    def request_eod_stock_values(self, stocks):
        parameters = {'access_key': api_token, 'symbols': ','.join(stocks)}
        return requests.get(market_stack_eod_endpoint, params=parameters)

if __name__ == '__main__':
    etl = LoadAccountValues()

    # Get stock symbols
    stocks = []
    result = etl.get_stocks()
    for row in result:
        stocks.append(row.symbol)

    # Get end of day closing stock values
    result = etl.request_eod_stock_values(stocks)
    eod_close_data = {}
    for each in result.json()['data']:
        eod_close_data[each['symbol']] = each['close']
    eod_close_json = json.dumps(eod_close_data)
    
    # Calculate new stock value based off share and closing value
    # Then update marek value table
    results = etl.get_account_stocks()
    for row in results:
        account_id = row.Account.account_id
        share_amount = row.Account.share_amount
        stock_symbol = row.Stock.symbol
        usd_account_amount = share_amount * Decimal(json.loads(eod_close_json)[stock_symbol])
        etl._account_value_dao.expire_account_value(account_id, usd_account_amount)