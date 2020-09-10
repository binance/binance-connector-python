from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def margin_transfer(self, asset: str, amount, type: int, **kwargs):
    """ Margin Account Transfer (MARGIN)
    Execute transfer between spot account and margin account.

    POST /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-transfer-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount'], [type, 'type']])

    payload = {'asset': asset, 'amount': amount, 'type': type, **kwargs}
    return self.sign_request('POST', '/sapi/v1/margin/transfer', payload)


def margin_borrow(self, asset: str, amount, **kwargs):
    """ Margin Account Borrow (MARGIN)
    Apply for a loan.

    POST /sapi/v1/margin/load

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-borrow-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount']])

    payload = {'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', '/sapi/v1/margin/loan', payload)


def margin_repay(self, asset: str, amount, **kwargs):
    """ Margin Account Repay(MARGIN)
    Repay loan for margin account.

    POST /sapi/v1/margin/repay

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-repay-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount']])

    payload = {'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', '/sapi/v1/margin/repay', payload)


def margin_asset(self, asset: str, **kwargs):
    """ Query Margin Asset (MARKET_DATA)

    GET /sapi/v1/margin/asset

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-asset-market_data

    """

    check_required_parameter(asset, 'asset')

    payload = {'asset': asset, **kwargs}
    return self.limit_request('GET', '/sapi/v1/margin/asset', payload)


def margin_pair(self, symbol: str, **kwargs):
    """ Query Margin Pair (MARKET_DATA)

    GET /sapi/v1/margin/pair

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-pair-market_data

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    """

    check_required_parameter(symbol, 'symbol')

    payload = {'symbol': symbol, **kwargs}
    return self.limit_request('GET', '/sapi/v1/margin/pair', payload)


def margin_all_assets(self, **kwargs):
    """ Get All Margin Assets (MARKET_DATA)

    GET /sapi/v1/margin/allAssets

    https://binance-docs.github.io/apidocs/spot/en/#get-all-margin-assets-market_data

    """

    return self.limit_request('GET', '/sapi/v1/margin/allAssets', kwargs)


def margin_all_pairs(self, **kwargs):
    """ Get All Margin Pairs (MARKET_DATA)

    GET /sapi/v1/margin/allPairs

    https://binance-docs.github.io/apidocs/spot/en/#get-all-margin-pairs-market_data

    """

    return self.limit_request('GET', '/sapi/v1/margin/allPairs', kwargs)


def margin_pair_index(self, symbol: str, **kwargs):
    """ Query Margin PriceIndex (MARKET_DATA)

    GET /sapi/v1/margin/priceIndex

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-priceindex-market_data

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    """

    check_required_parameter(symbol, 'symbol')
    payload = {'symbol': symbol, **kwargs}
    return self.limit_request('GET', '/sapi/v1/margin/priceIndex', payload)


def new_margin_order(self, symbol: str, side: str, type: str, quantity: str, **kwargs):
    """ Margin Account New Order (TRADE)

    Post a new order for margin account.

    POST /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-new-order-trade

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    side -- mandatory/string
    type -- mandatory/string
    quantity -- mandatory/string
    """

    check_required_parameters([
        [symbol, 'symbol'],
        [side, 'side'],
        [type, 'type'],
        [quantity, 'quantity']
    ])

    payload = {
        'symbol': symbol,
        'side': side,
        'type': type,
        'quantity': quantity,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/margin/order', payload)


def cancel_margin_order(self, symbol: str, **kwargs):
    """ Margin Account Cancel Order (TRADE)

     Cancel an active order for margin account.

    DELETE /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-order-trade

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    """
    check_required_parameter(symbol, 'symbol')
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('DELETE', '/sapi/v1/margin/order', payload)


def margin_transfer_history(self, asset: str, **kwargs):
    """ Get Transfer History (USER_DATA)

    GET /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-transfer-history-user_data

    Parameteres:
    asset -- mandatory/string
    """
    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/transfer', payload)


def margin_load_record(self, asset: str, **kwargs):
    """ Query Loan Record (USER_DATA)

    GET /sapi/v1/margin/loan

    https://binance-docs.github.io/apidocs/spot/en/#query-loan-record-user_data

    Parameteres:
    asset -- mandatory/string
    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/loan', payload)


def margin_repay_record(self, asset: str, **kwargs):
    """ Query Repay Record (USER_DATA)

    GET /sapi/v1/margin/repay

    https://binance-docs.github.io/apidocs/spot/en/#query-repay-record-user_data

    Parameteres:
    asset -- mandatory/string
    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/repay', payload)


def margin_interest_history(self, **kwargs):
    """ Get Interest History (USER_DATA)

    GET /sapi/v1/margin/interestHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data

    """

    return self.sign_request('GET', '/sapi/v1/margin/interestHistory', kwargs)


def margin_force_liquidation_record(self, **kwargs):
    """ Get Force Liquidation Record (USER_DATA)

    GET /sapi/v1/margin/forceLiquidationRec

    https://binance-docs.github.io/apidocs/spot/en/#get-force-liquidation-record-user_data

    """

    return self.sign_request('GET', '/sapi/v1/margin/forceLiquidationRec', kwargs)


def margin_account(self, **kwargs):
    """ Query Margin Account Details (USER_DATA)

    GET /sapi/v1/margin/account

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-details-user_data

    """

    return self.sign_request('GET', '/sapi/v1/margin/account', kwargs)


def margin_order(self, symbol: str, **kwargs):
    """ Query Margin Account's Order (USER_DATA)

    GET /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-order-user_data

    """

    check_required_parameter(symbol, 'symbol')
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/order', payload)


def margin_open_orders(self, **kwargs):
    """ Query Margin Account's Open Order (USER_DATA)

    GET /sapi/v1/margin/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-open-order-user_data

    """

    return self.sign_request('GET', '/sapi/v1/margin/openOrders', kwargs)


def margin_all_orders(self, symbol: str, **kwargs):
    """ Query Margin Account's All Orders (USER_DATA)

    GET /sapi/v1/margin/allOrders

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-all-order-user_data

    """

    check_required_parameter(symbol, 'symbol')
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/allOrders', payload)


def margin_my_trades(self, symbol: str, **kwargs):
    """ Query Margin Account's Trade List (USER_DATA)

    GET /sapi/v1/margin/myTrades

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-trade-list-user_data

    """

    check_required_parameter(symbol, 'symbol')

    payload = {'symbol': symbol, **kwargs}

    return self.sign_request('GET', '/sapi/v1/margin/myTrades', payload)


def margin_max_borrowable(self, asset: str, **kwargs):
    """ Query Max Borrow (USER_DATA)

    GET /sapi/v1/margin/maxBorrowable

    https://binance-docs.github.io/apidocs/spot/en/#query-max-borrow-user_data

    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/maxBorrowable', payload)


def margin_max_transferable(self, asset: str, **kwargs):
    """ Query Max Transfer-Out Amount (USER_DATA)

    GET /sapi/v1/margin/maxTransferable

    https://binance-docs.github.io/apidocs/spot/en/#query-max-transfer-out-amount-user_data

    """

    check_required_parameter(asset, 'asset')
    payload = {'asset': asset, **kwargs}
    return self.sign_request('GET', '/sapi/v1/margin/maxBorrowable', payload)

def new_isolate_margin_account(self, base: str, quote: str, **kwargs):
    """ Create Isolated Margin Account (MARGIN)

    POST /sapi/v1/margin/isolated/create

    https://binance-docs.github.io/apidocs/spot/en/#query-max-transfer-out-amount-user_data

    Parameteres:
    | base       | mandatory | string | Base aseet of symbol  |
    | quote      | mandatory | string | Quote asset of symbol |
    | recvWindow | optional  | int    |                       |
    """

    check_required_parameters([
        [base, 'base'],
        [quote, 'quote']
    ])

    payload = {
        'base': base,
        'quote': quote,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/margin/isolated/create', payload)


def isolate_margin_transfer(self, asset: str, symbol: str, transFrom: str, transTo: str, amount, **kwargs):
    """ Isolated Margin Account Transfer (MARGIN)

    POST /sapi/v1/margin/isolated/transfer

    https://binance-docs.github.io/apidocs/spot/en/#isolated-margin-account-transfer-margin

    Parameteres:
    | asset      | mandatory | string | asset,such as BTC         |
    | symbol     | mandatory | string |                           |
    | transFrom  | mandatory | string | "SPOT", "ISOLATED_MARGIN" |
    | transTo    | mandatory | string | "SPOT", "ISOLATED_MARGIN" |
    | amount     | mandatory | float  |                           |
    | recvWindow | optional  | int    |                           |
    """

    check_required_parameters([
        [asset, 'asset'],
        [symbol, 'symbol'],
        [transFrom, 'transFrom'],
        [transTo, 'transTo'],
        [amount, 'amount'],
    ])

    payload = {
        'asset': asset,
        'symbol': symbol,
        'transFrom': transFrom,
        'transTo': transTo,
        'amount': amount,
        **kwargs
    }
    return self.sign_request('POST', '/sapi/v1/margin/isolated/transfer', payload)

def isolate_margin_transfer_history(self, symbol: str, **kwargs):
    """ Get Isolated Margin Transfer History (USER_DATA)

    GET /sapi/v1/margin/isolated/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-isolated-margin-transfer-history-user_data

    Parameteres:
    | asset      | optional  | string | asset,such as BTC         |
    | symbol     | mandatory | string |                           |
    | transFrom  | optional  | string | "SPOT", "ISOLATED_MARGIN" |
    | transTo    | optional  | string | "SPOT", "ISOLATED_MARGIN" |
    | startTime  | optional  | int    |                           |
    | endTime    | optional  | int    |                           |
    | current    | optional  | int    | Current page, default 1   |
    | size       | optional  | int    | Default 10, max 100       |
    | recvWindow | optional  | int    |                           |
    """

    check_required_parameter(symbol, 'symbol')

    payload = {
        'symbol': symbol,
        **kwargs
    }
    return self.sign_request('GET', '/sapi/v1/margin/isolated/transfer', payload)


def isolate_margin_account(self, **kwargs):
    """ Query Isolated Margin Account Info (USER_DATA)

    GET /sapi/v1/margin/isolated/account

    https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data

    Parameteres:
    | symbols    | optional | string | Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT" |
    | recvWindow | optional | int    |                                                                             |
    """
    
    return self.sign_request('GET', '/sapi/v1/margin/isolated/account', kwargs)


def isolate_margin_pair(self, symbol: str, **kwargs):
    """ Query Isolated Margin Symbol (USER_DATA)

    GET /sapi/v1/margin/isolated/pair

    https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data

    Parameteres:
    | symbol     | mandatory | string |
    | recvWindow | optional  | int    |
    """

    check_required_parameter(symbol, 'symbol')

    payload = {
        'symbol': symbol,
        **kwargs
    }
    
    return self.sign_request('GET', '/sapi/v1/margin/isolated/pair', payload)


def isolate_margin_pair(self, symbol: str, **kwargs):
    """ Query Isolated Margin Symbol (USER_DATA)

    GET /sapi/v1/margin/isolated/pair

    https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data

    Parameteres:
    | symbol     | mandatory | string |
    | recvWindow | optional  | int    |
    """

    check_required_parameter(symbol, 'symbol')

    payload = {
        'symbol': symbol,
        **kwargs
    }
    
    return self.sign_request('GET', '/sapi/v1/margin/isolated/pair', payload)


def isolate_margin_all_pairs(self, **kwargs):
    """ Get All Isolated Margin Symbol(USER_DATA)

    GET /sapi/v1/margin/isolated/allPairs

    https://binance-docs.github.io/apidocs/spot/en/#get-all-isolated-margin-symbol-user_data

    Parameteres:
    | recvWindow | optional | int    |                                                                             |
    """
    
    return self.sign_request('GET', '/sapi/v1/margin/isolated/allPairs', kwargs)
