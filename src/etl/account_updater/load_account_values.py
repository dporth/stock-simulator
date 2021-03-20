import sys
[sys.path.append(i) for i in ['.', '..','../../../']]
import requests
import json
from decimal import Decimal
from src.config import polygon_stock_price_updated_key, polygon_stock_eod_endpoint
from src.dao.stock_price_queue_dao import StockPriceQueueDAO
from src.dao.stock_price_history_dao import StockPriceHistoryDAO
from src.dao.stock_dao import StockDAO
from src.dao.account_dao import AccountDAO
from src.dao.account_value_dao import AccountValueDAO

class LoadAccountValues():
    def __init__(self):
        self._queue = StockPriceQueueDAO()
        self._stock = StockDAO()
        self._stock_history = StockPriceHistoryDAO()
        self._account = AccountDAO()
        self._account_value = AccountValueDAO()

    def get_account_stocks(self):
        """Returns all accounts with their stocks in a list of dictionaries."""
        accounts = []
        result = self._account.get_accounts_to_refresh()
        for row in result:
            account = {"account_id": row.Account.account_id, "stock_id":row.Account.stock_id, 'share_amount': row.Account.share_amount}
            accounts.append(account)
        return accounts

    def get_stock_symbol(self, stock_id):
        """Gets symbol from stock id."""
        result = self._stock.get_stock_by_id(stock_id).first()
        if result:
            symbol = result.symbol
        return symbol

    def update_stock_price_history(self, stock_id, value):
        """Takes in a symbol and value and updates the historical usd account value in stock price history table."""
        return self._stock_history.update_stock_value(stock_id, value)

    def request_eod_stock_values(self, symbol):
        """Sends a request to stock market api to retrieve the latest prices for the stock."""
        return requests.get(polygon_stock_eod_endpoint.format(ticker=symbol, key=polygon_stock_price_updated_key))

    def update_account_values(self, account_id, eod_value, share_amount):
        """Creates a stock account value for each stock account that is for the specified stock_id."""
        self._account_value.expire_account_value(account_id, share_amount*Decimal(eod_value))

if __name__ == '__main__':
    etl = LoadAccountValues()
    accounts = etl.get_account_stocks() 
    for i in range(1,6): # Can only make 5 api calls per minute, so regardless of the number of stock accounts only deal with 5 at a time
        if i-1 >= len(accounts):
            break
        else:
            account = accounts[i-1]
            stock_id = account['stock_id']
            symbol = etl.get_stock_symbol(stock_id)
            response = etl.request_eod_stock_values(symbol)
            eod_value = json.loads(response.text)['results'][0]['c']
            etl.update_account_values(account['account_id'], eod_value, account['share_amount'])
            etl.update_stock_price_history(stock_id, eod_value)






