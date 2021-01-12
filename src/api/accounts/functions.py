from src.dao.user_dao import UserDAO
from src.dao.account_dao import AccountDAO
from src.dao.stock_dao import StockDAO
from datetime import datetime

def get_accounts():
    """Returns a list of all accounts from the account table."""
    response = {}

    account_dao = AccountDAO()
    result = account_dao.get_accounts()
    return process_response(result)

def get_account_by_id(account_id):
    """Returns all accounts specified by the provided account id."""
    response = {}
    successful_response = {}
    error_response = {}

    account_dao = AccountDAO()
    result = account_dao.get_account_by_id(account_id)
    if len(result.all()) != 0:
        return process_response(result)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

def delete_account(account_id):
    """Deletes an account and all account values that belong to the account."""
    response = {}
    successful_response = {}
    error_response = {}

    account_dao = AccountDAO()
    result = account_dao.get_account_by_id(account_id)
    if len(result.all()) != 0:
        deleted_account = account_dao.delete_account(account_id)
        successful_response['account_id'] = deleted_account
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response
    response['data'] = successful_response
    response['timestamp'] = datetime.utcnow()
    return response

def create_account(json):
    response = {}
    successful_response = {}
    error_response = {}

    account_dao = AccountDAO()
    stock_dao = StockDAO()
    user_dao = UserDAO()
    
    if not required_keys(json, ['usd_amount', 'share_amount', 'symbol', 'user_id']):
        error_response['message'] = "Request body is missing required key value pairs. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    usd_amount = json['usd_amount']
    share_amount = json['share_amount']
    symbol = json['symbol']
    user_id = json['user_id']

    # Ensure usd and share amount are not strings
    if not isinstance(usd_amount, (int, float)) or not isinstance(share_amount, (int, float)):
        # not a number
        error_response['message'] = "The request json contains a string when a number is expected. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    # Get stock id
    result = stock_dao.get_stock_by_symbol(symbol).first()
    if result:
        stock_id = result.stock_id
    else:
        # stock not found
        error_response['message'] = "Could not find stock provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    # Check to see if user exists
    result = user_dao.get_user_by_id(user_id).first()
    if result:
        user_id = result.User.user_id
    else:
        # user not found
        error_response['message'] = "Could not find user provided. Invalid request."
        error_response['code'] = '400'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

    # Create account
    new_account = account_dao.create_account(usd_amount, share_amount, stock_id, user_id)

    successful_response['account_id'] = new_account
    successful_response['stock_id'] = stock_id
    successful_response['user_id'] = user_id
    successful_response['usd_amount'] = usd_amount
    successful_response['share_amount'] = share_amount
    response['data'] = successful_response
    response['timestamp'] = datetime.utcnow()
    return response

def required_keys(json, required):
    """Takes in a list of required keys and checks to see if each key in the json is present in the array of required keys.
    Returns True if all keys required are present otherwise returns False.
    """
    keys_found = []
    for each in json.keys():
        if each in required:
            keys_found.append(each)
    return set(keys_found) == set(required)

def historical_account_values(account_id):
    """Returns a json containing the historical account values for the specified account id"""
    account_dao = AccountDAO()
    query = account_dao.get_account_values(account_id)
    history = []
    for row in query:
        current_row = {}
        current_row['valid_from'] = row.AccountValue.valid_from
        current_row['valid_to'] = row.AccountValue.valid_to
        current_row['usd_account_value'] = str(row.AccountValue.usd_account_amount)
        history.append(current_row)
    return history

def process_response(query):
    """Takes a query and formats the attributes in the query. Returns the formatted attributes."""
    response = {}
    accounts = []   
    for row in query:
        account = {}
        account['account_id'] = row.Account.account_id
        if row.AccountValue == None:
            current_usd_account_value = None
        else:
            current_usd_account_value = str(row.AccountValue.usd_account_amount)
        account['current_usd_account_value'] = current_usd_account_value
        account['usd_amount'] = str(row.Account.usd_amount)
        account['share_amount'] = str(row.Account.share_amount)
        account['historical_account_values'] = historical_account_values(row.Account.account_id)
        account['user'] = {'first_name': row.User.first_name, 'last_name': row.User.last_name, 'user_id': row.User.user_id}
        account['stock'] = {'symbol': row.Stock.symbol, 'stock_id': row.Stock.stock_id}
        accounts.append(account)
    response['data'] = accounts
    response['timestamp'] = datetime.utcnow()
    return response