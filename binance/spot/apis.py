from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def ping(self):
    """ Test Connectivity
    Test connectivity to the Rest API.

    GET /api/v3/ping

    https://binance-docs.github.io/apidocs/spot/en/#test-connectivity

    """

    url_path = '/api/v3/ping'
    return self.query(url_path)


def time(self):
    """ Check Server Time
    Test connectivity to the Rest API and get the current server time.

    GET /api/v3/time

    https://binance-docs.github.io/apidocs/spot/en/#check-server-time

    """

    url_path = '/api/v3/time'
    return self.query(url_path)


def exchange_info(self):
    """ Exchange Information
    Current exchange trading rules and symbol information

    GET /api/v3/exchangeinfo

    https://binance-docs.github.io/apidocs/spot/en/#exchange-information

    """

    url_path = '/api/v3/exchangeInfo'
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """ get orderbook.

    GET /api/v3/depth

    https://binance-docs.github.io/apidocs/spot/en/#order-book

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    limit -- optional/integer -- limit the results
                                    Default 100
                                    max 1000
                                    Valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]
    """

    check_required_parameter(symbol, 'symbol')
    params = {'symbol': symbol, **kwargs}
    return self.query('/api/v3/depth', params)


def trades(self, symbol: str, **kwargs):
    """ Recent Trades List
    Get recent trades (up to last 500).

    GET /api/v3/trades

    https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    limit -- optional/integer -- limit the results
                                    Default 500
                                    max 1000
    """
    check_required_parameter(symbol, 'symbol')
    params = {'symbol': symbol, **kwargs}
    return self.query('/api/v3/trades', params)


def historical_trades(self, symbol: str, **kwargs):
    """ Old Trade Lookup
    Get older market trades.

    GET /api/v3/historicalTrades

    https://binance-docs.github.io/apidocs/spot/en/#old-trade-lookup

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    limit -- optional/integer -- limit the results
                                    Default 500
                                    max 1000
    formId -- optional/integer -- trade id to fetch from. Default gets most recent trades.
    """
    check_required_parameter(symbol, 'symbol')
    params = {'symbol': symbol, **kwargs}
    return self.limit_request('GET', '/api/v3/historicalTrades', params)


def agg_trades(self, symbol: str, **kwargs):
    """ Compressed/Aggregate Trades List

    GET /api/v3/aggTrades

    https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    limit -- optional/integer -- limit the results
                                    Default 500
                                    max 1000
    formId -- optional/integer -- id to get aggregate trades from INCLUSIVE.
    startTime -- optional/timestamp -- Timestamp in ms to get aggregate trades from INCLUSIVE.
    endTime -- optional/timestamp -- Timestamp in ms to get aggregate trades until INCLUSIVE.
    """

    check_required_parameter(symbol, 'symbol')
    params = {'symbol': symbol, **kwargs}
    return self.query('/api/v3/aggTrades', params)


def klines(self, symbol: str, interval: str, **kwargs):
    """ Kline/Candlestick Data

    GET /api/v3/klines

    https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    interval -- mandatory/string -- the interval of kline
                                    e.g 1m, 5m, 1h, 1d, etc
    limit -- optional/integer -- limit the results
                                    Default 500
                                    max 1000
    startTime -- optional/timestamp
    endTime -- optional/timestamp
    """
    check_required_parameters([[symbol, 'symbol'], [interval, 'interval']])

    params = {
        'symbol': symbol,
        'interval': interval,
        **kwargs
    }
    return self.query('/api/v3/klines', params)


def avg_price(self, symbol: str):
    """ Current Average Price

    GET /api/v3/avgPrice

    https://binance-docs.github.io/apidocs/spot/en/#current-average-price

    Parameteres:
    symbol -- mandatory/string -- the trading pair
    """

    check_required_parameter(symbol, 'symbol')
    params = {
        'symbol': symbol,
    }
    return self.query('/api/v3/avgPrice', params)


def ticker_24hr(self, symbol: str = None):
    """ 24hr Ticker Price Change Statistics

    GET /api/v3/ticker/24hr

    https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

    Parameteres:
    symbol -- optional/string -- the trading pair
    """

    params = {
        'symbol': symbol,
    }
    return self.query('/api/v3/ticker/24hr', params)


def ticker_price(self, symbol: str = None):
    """ Symbol Price Ticker

    GET /api/v3/ticker/price

    https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker

    Parameteres:
    symbol -- optional/string -- the trading pair
    """

    params = {
        'symbol': symbol,
    }
    return self.query('/api/v3/ticker/price', params)


def book_ticker(self, symbol: str = None):
    """ Symbol Order Book Ticker

    GET /api/v3/ticker/bookTicker

    https://binance-docs.github.io/apidocs/spot/en/#symbol-order-book-ticker

    Parameteres:
    symbol -- optional/string -- the trading pair
    """

    params = {
        'symbol': symbol,
    }
    return self.query('/api/v3/ticker/bookTicker', params)


def new_order_test(self, **kwargs):
    """ Test New Order (TRADE)

    Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

    POST /api/v3/order/test

    https://binance-docs.github.io/apidocs/spot/en/#test-new-order-trade
    """

    url_path = '/api/v3/order/test'
    return self.sign_request('POST', url_path, {**kwargs})


def new_order(self, **kwargs):
    """ New OCO (TRADE)

    Post a new order

    POST /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
    """

    url_path = '/api/v3/order'
    return self.sign_request('POST', url_path, {**kwargs})


def cancel_order(self, symbol: str, **kwargs):
    """ Cancel Order (TRADE)

    Cancel an active order.

    DELETE /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade
    """
    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/order'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('DELETE', url_path, payload)


def cancel_open_orders(self, symbol, **kwargs):
    """ Cancel all Open Orders on a Symbol (TRADE)

    Cancels all active orders on a symbol.
    This includes OCO orders.

    DELETE api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade
    """
    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/openOrders'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('DELETE', url_path, payload)


def get_order(self, symbol, **kwargs):
    """ Query Order (USER_DATA)

    Check an order's status.

    GET /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data
    """
    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/order'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', url_path, payload)


def get_open_orders(self, symbol=None, **kwargs):
    """ Current Open Orders (USER_DATA)

    Get all open orders on a symbol.

    GET /api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data
    """

    url_path = '/api/v3/openOrders'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', url_path, payload)


def get_orders(self, symbol: str, **kwargs):
    """ All Orders (USER_DATA)

    Get all account orders; active, canceled, or filled.

    GET /api/v3/allOrders

    https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data
    """
    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/allOrders'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', url_path, payload)


def new_oco_order(self, **kwargs):
    """ New OCO (TRADE)

    Post a new oco order

    POST /api/v3/order/oco

    https://binance-docs.github.io/apidocs/spot/en/#new-oco-trade
    """

    url_path = '/api/v3/order/oco'
    return self.sign_request('POST', url_path, {**kwargs})


def cancel_oco_order(self, symbol, **kwargs):
    """ Cancel OCO (TRADE)

    Cancel an entire Order List

    DELETE /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#cancel-oco-trade
    """
    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/orderList'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('DELETE', url_path, payload)


def get_oco_order(self, **kwargs):
    """ Query OCO (USER_DATA)

    Retrieves a specific OCO based on provided optional parameters

    GET /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#query-oco-user_data
    """
    url_path = '/api/v3/orderList'
    return self.sign_request('GET', url_path, {**kwargs})


def get_oco_orders(self, **kwargs):
    """ Query all OCO (USER_DATA)

    Retrieves all OCO based on provided optional parameters

    GET /api/v3/allOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-all-oco-user_data
    """

    url_path = '/api/v3/allOrderList'
    return self.sign_request('GET', url_path, {**kwargs})


def get_oco_open_orders(self, **kwargs):
    """ Query Open OCO (USER_DATA)

    GET /api/v3/openOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-open-oco-user_data
    """

    url_path = '/api/v3/openOrderList'
    return self.sign_request('GET', url_path, {**kwargs})


def account(self, **kwargs):
    """ Account Information (USER_DATA)

    Get current account information

    GET /api/v3/account

    https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data
    """

    url_path = '/api/v3/account'
    return self.sign_request('GET', url_path, {**kwargs})


def my_trades(self, symbol: str, **kwargs):
    """ Account Trade List (USER_DATA)

    Get trades for a specific account and symbol.

    GET /api/v3/myTrades

    https://binance-docs.github.io/apidocs/spot/en/#account-trade-list-user_data
    """

    check_required_parameter(symbol, 'symbol')

    url_path = '/api/v3/myTrades'
    payload = {'symbol': symbol, **kwargs}
    return self.sign_request('GET', url_path, payload)
