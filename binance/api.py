from urllib.parse import urlencode
from binance.lib.utils import cleanNoneValue
from binance.lib.utils import check_required_parameter
from . import version
import requests

class API(object):

    def __init__(self, key=None, secrect=None):
        self.key = key
        self.secret = secrect
        self.baseUrl = 'https://api.binance.com'
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json;charset=utf-8'})
        self.session.headers.update({
            'User-Agent': 'binance-python/' + version.__version__
        })
        if self.key is not None:
            self.session.headers.update({'X-MBX-APIKEY': self.key})
        self.response = None
        return

    def ping(self):
        """ Test Connectivity
        Test connectivity to the Rest API.

        GET /api/v3/ping

        https://binance-docs.github.io/apidocs/spot/en/#test-connectivity

        """

        urlPath = '/api/v3/ping'
        return self._query(urlPath)

    def time(self):
        """ Check Server Time
        Test connectivity to the Rest API and get the current server time.

        GET /api/v3/time

        https://binance-docs.github.io/apidocs/spot/en/#check-server-time

        """

        urlPath = '/api/v3/time'
        return self._query(urlPath)

    def exchange_info(self):
        """ Exchange Information
        Current exchange trading rules and symbol information

        GET /api/v3/exchangeinfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

        """

        urlPath = '/api/v3/exchangeInfo'
        return self._query(urlPath)

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
        return self._query('/api/v3/depth', self._prepare_params(params))

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
        return self._query('/api/v3/trades', self._prepare_params(params))

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
        return self._query('/api/v3/historicalTrades', self._prepare_params(params))

    def agg_trades(self, symbol:str, limit:int=500, fromId=None, startTime=None, endTime=None):
        params = {
            'symbol': symbol,
            'limit': limit,
            'fromId': fromId,
            'startTime': startTime,
            'endTime': endTime
        }
        return self._query('/api/v3/aggTrades', self._prepare_params(params))

    def klines(self, symbol:str, interval:str, limit:int=500, startTime=None, endTime=None) -> any:
        params = {
            'symbol':    symbol,
            'interval':  interval,
            'limit':     limit,
            'startTime': startTime,
            'endTime':   endTime
        }
        return self._query('/api/v3/klines', self._prepare_params(params))

    def avg_price(self, symbol):
        params = {
            'symbol': symbol,
        }
        return self._query('/api/v3/avgPrice', self._prepare_params(params))

    def ticker_24hr(self, symbol):
        params = {
            'symbol': symbol,
        }
        return self._query('/api/v3/ticker/24hr', self._prepare_params(params))

    def ticker_price(self, symbol):
        params = {
            'symbol': symbol,
        }
        return self._query('/api/v3/ticker/price', self._prepare_params(params))

    def book_ticker(self, symbol):
        params = {
            'symbol': symbol,
        }
        return self._query('/api/v3/ticker/bookTicker', self._prepare_params(params))

    def _prepare_params(self, params):
        return urlencode(cleanNoneValue(params))

    def _query(self, urlPath, payload={}):
        url = self.baseUrl + urlPath
        return self.session.get(url, params=payload)
