from urllib.parse import urlencode
from binance.lib.utils import cleanNoneValue
from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.api import API

class Market(API):

    def ping(self):
        """ Test Connectivity
        Test connectivity to the Rest API.

        GET /api/v3/ping

        https://binance-docs.github.io/apidocs/spot/en/#test-connectivity

        """

        urlPath = '/api/v3/ping'
        return self.query(urlPath)

    def time(self):
        """ Check Server Time
        Test connectivity to the Rest API and get the current server time.

        GET /api/v3/time

        https://binance-docs.github.io/apidocs/spot/en/#check-server-time

        """

        urlPath = '/api/v3/time'
        return self.query(urlPath)

    def exchange_info(self):
        """ Exchange Information
        Current exchange trading rules and symbol information

        GET /api/v3/exchangeinfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

        """

        urlPath = '/api/v3/exchangeInfo'
        return self.query(urlPath)

    def depth(self, symbol: str, limit: int = 100):
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
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return self.query('/api/v3/depth', self._prepare_params(params))

    def trades(self, symbol: str, limit: int = 500):
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
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return self.query('/api/v3/trades', self._prepare_params(params))

    def historical_trades(self, symbol: str, limit: int = 500, fromId: int = None):
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
        params = {
            'symbol': symbol,
            'limit':  limit,
            'fromId': fromId
        }
        return self.query('/api/v3/historicalTrades', self._prepare_params(params))

    def agg_trades(self, symbol: str, limit: int = 500, fromId=None, startTime=None, endTime=None):
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
        params = {
            'symbol':    symbol,
            'limit':     limit,
            'fromId':    fromId,
            'startTime': startTime,
            'endTime':   endTime
        }
        return self.query('/api/v3/aggTrades', self._prepare_params(params))

    def klines(self, symbol: str, interval: str, limit: int = 500, startTime=None, endTime=None):
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
            'symbol':    symbol,
            'interval':  interval,
            'limit':     limit,
            'startTime': startTime,
            'endTime':   endTime
        }
        return self.query('/api/v3/klines', self._prepare_params(params))

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
        return self.query('/api/v3/avgPrice', self._prepare_params(params))

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
        return self.query('/api/v3/ticker/24hr', self._prepare_params(params))

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
        return self.query('/api/v3/ticker/price', self._prepare_params(params))

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
        return self.query('/api/v3/ticker/bookTicker', self._prepare_params(params))
