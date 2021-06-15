from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def ping(self):
    """Test Connectivity
    Test connectivity to the Rest API.

    GET /api/v3/ping

    https://binance-docs.github.io/apidocs/spot/en/#test-connectivity

    """

    url_path = "/api/v3/ping"
    return self.query(url_path)


def time(self):
    """Check Server Time
    Test connectivity to the Rest API and get the current server time.

    GET /api/v3/time

    https://binance-docs.github.io/apidocs/spot/en/#check-server-time

    """

    url_path = "/api/v3/time"
    return self.query(url_path)


def exchange_info(self):
    """Exchange Information
    Current exchange trading rules and symbol information

    GET /api/v3/exchangeinfo

    https://binance-docs.github.io/apidocs/spot/en/#exchange-information

    """

    url_path = "/api/v3/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """Get orderbook.

    GET /api/v3/depth

    https://binance-docs.github.io/apidocs/spot/en/#order-book

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 100; valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/api/v3/depth", params)


def trades(self, symbol: str, **kwargs):
    """Recent Trades List
    Get recent trades (up to last 500).

    GET /api/v3/trades

    https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/api/v3/trades", params)


def historical_trades(self, symbol: str, **kwargs):
    """Old Trade Lookup
    Get older market trades.

    GET /api/v3/historicalTrades

    https://binance-docs.github.io/apidocs/spot/en/#old-trade-lookup

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        formId (int, optional): trade id to fetch from. Default gets most recent trades.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/api/v3/historicalTrades", params)


def agg_trades(self, symbol: str, **kwargs):
    """Compressed/Aggregate Trades List

    GET /api/v3/aggTrades

    https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        formId (int, optional): id to get aggregate trades from INCLUSIVE.
        startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/api/v3/aggTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    """Kline/Candlestick Data

    GET /api/v3/klines

    https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

    Args:
        symbol (str): the trading pair
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])

    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/api/v3/klines", params)


def avg_price(self, symbol: str):
    """Current Average Price

    GET /api/v3/avgPrice

    https://binance-docs.github.io/apidocs/spot/en/#current-average-price

    Args:
        symbol (str): the trading pair
    """

    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.query("/api/v3/avgPrice", params)


def ticker_24hr(self, symbol: str = None):
    """24hr Ticker Price Change Statistics

    GET /api/v3/ticker/24hr

    https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

    Args:
        symbol (str, optional): the trading pair
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/api/v3/ticker/24hr", params)


def ticker_price(self, symbol: str = None):
    """Symbol Price Ticker

    GET /api/v3/ticker/price

    https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker

    Args:
        symbol (str, optional): the trading pair
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/api/v3/ticker/price", params)


def book_ticker(self, symbol: str = None):
    """Symbol Order Book Ticker

    GET /api/v3/ticker/bookTicker

    https://binance-docs.github.io/apidocs/spot/en/#symbol-order-book-ticker

    Args:
        symbol (str, optional): the trading pair
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/api/v3/ticker/bookTicker", params)
