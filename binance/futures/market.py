from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def ping(self):
    """Test Connectivity
    Test connectivity to the Rest API.

    GET /fapi/v1/ping

    https://binance-docs.github.io/apidocs/futures/en/#test-connectivity

    """

    url_path = "/fapi/v1/ping"
    return self.query(url_path)


def time(self):
    """Check Server Time
    Test connectivity to the Rest API and get the current server time.

    GET /fapi/v1/time

    https://binance-docs.github.io/apidocs/futures/en/#check-server-time

    """

    url_path = "/fapi/v1/time"
    return self.query(url_path)


def exchange_info(self):
    """Exchange Information
    Current exchange trading rules and symbol information

    GET /fapi/v1/exchangeInfo

    https://binance-docs.github.io/apidocs/futures/en/#exchange-information

    """

    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """Order Book
    Get order book.

    GET /fapi/v1/depth

    https://binance-docs.github.io/apidocs/futures/en/#order-book

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000]
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/depth", params)


def trades(self, symbol: str, **kwargs):
    """Recent Trades List
    Get recent trades (up to last 500).

    GET /fapi/v1/trades

    https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/trades", params)


def historical_trades(self, symbol: str, **kwargs):
    """Old Trades Lookup (MARKET_DATA)
    Get older market historical trades.

    GET /fapi/v1/historicalTrades

    https://binance-docs.github.io/apidocs/futures/en/#old-trade-lookup

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        formId (int, optional): trade id to fetch from. Default gets most recent trades.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/fapi/v1/historicalTrades", params)


def agg_trades(self, symbol: str, **kwargs):
    """Compressed/Aggregate Trades List
    Get compressed, aggregate market trades. Market trades that fill at the time, from the same order,
    with the same price will have the quantity aggregated.

    GET /fapi/v1/aggTrades

    https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

    Args:
        symbol (str): the trading pair
    Keyword Args:
        formId (int, optional): id to get aggregate trades from INCLUSIVE.
        startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
        limit (int, optional): limit the results. Default 500; max 1000.
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/aggTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    """Kline/Candlestick Data
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

    GET /fapi/v1/klines

    https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data

    Args:
        symbol (str): the trading pair
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
    Keyword Args:
        startTime (int, optional): Timestamp in ms to get klines from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get klines until INCLUSIVE.
        limit (int, optional): limit the results. Default 500; max 1000.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])

    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/klines", params)


def continuous_klines(self, pair: str, contract_type: str, interval: str, **kwargs):
    """Continuous Contract Kline/Candlestick Data
    Continuous Kline/candlestick bars for a specific contract type.

    GET /fapi/v1/continuousKlines

    https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data

    Args:
        pair (str): the trading pair
        contract_type : the type of contract
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
    Keyword Args:
        startTime (int, optional): Timestamp in ms to get continuous klines from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get continuous klines until INCLUSIVE.
        limit (int, optional): limit the results. Default 500; max 1500.
    """
    check_required_parameters([[pair, "pair"], [contract_type, "contractType"], [interval, "interval"]])
    params = {"pair": pair, "contractType": contract_type, "interval": interval, **kwargs}
    return self.query("/fapi/v1/continuousKlines", params)


def index_price_klines(self, pair: str, interval: str, **kwargs):
    """Index Price Kline/Candlestick Data
    Kline/candlestick bars for the index price of a pair.

    GET /fapi/v1/indexPriceKlines

    https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data

    Args:
        pair (str): the trading pair
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
    Keyword Args:
        startTime (int, optional): Timestamp in ms to get index price klines from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get index price klines until INCLUSIVE.
        limit (int, optional): limit the results. Default 500; max 1500.
    """
    check_required_parameters([[pair, "pair"], [interval, "interval"]])
    params = {"pair": pair, "interval": interval, **kwargs}
    return self.query("/fapi/v1/indexPriceKlines", params)


def mark_price_klines(self, symbol: str, interval: str, **kwargs):
    """Mark Price Kline/Candlestick Data
    Kline/candlestick bars for the mark price of a symbol.

    GET /fapi/v1/markPriceKlines

    https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data

    Args:
        symbol (str): the trading pair
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
    Keyword Args:
        startTime (int, optional): Timestamp in ms to get mark price klines from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get mark price klines until INCLUSIVE.
        limit (int, optional): limit the results. Default 500; max 1500.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/markPriceKlines", params)


def mark_price(self, symbol: str = None):
    """Mark Price
    Mark Price and Funding Rate.

    GET /fapi/v1/premiumIndex

    https://binance-docs.github.io/apidocs/futures/en/#mark-price

    Args:
        symbol (str): the trading pair
    """
    params = {"symbol": symbol}
    return self.query("/fapi/v1/premiumIndex", params)


def funding_rate_history(self, symbol: str = None, **kwargs):
    """Get Funding Rate History
    Funding rate history

    GET /fapi/v1/fundingRate

    https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history

    Note:
       If startTime and endTime are not sent, the most recent limit data is returned.
       If the number of data between startTime and endTime is larger than limit, return as startTime + limit.
       In ascending order.
    Keyword Args:
        symbol (str, optional): the trading pair
        startTime (int, optional): Timestamp in ms to get funding rate from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get funding rate until INCLUSIVE.
        limit (int, optional): limit the results. Default 100; max 1000.
    """
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/fundingRate", params)


def ticker_24hr(self, symbol: str = None):
    """24hr Ticker Price Change Statistics
    24 hour rolling window price change statistics.
    Careful when accessing this with no symbol.

    GET /fapi/v1/ticker/24hr

    https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history

    Note:
       If the symbol is not sent, tickers for all symbols will be returned in an array.
    Keyword Args:
        symbol (str): the trading pair
    """
    params = {"symbol": symbol}
    return self.query("/fapi/v1/ticker/24hr", params)


def ticker_price(self, symbol: str = None):
    """Symbol Price Ticker
    Latest price for a symbol or symbols.


    GET /fapi/v1/ticker/price

    https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

    Note:
       If the symbol is not sent, tickers for all symbols will be returned in an array.
    Keyword Args:
        symbol (str): the trading pair
    """
    params = {"symbol": symbol}
    return self.query("/fapi/v1/ticker/price", params)


def book_ticker(self, symbol: str = None):
    """Symbol Order Book Ticker
    Best price/qty on the order book for a symbol or symbols.


    GET /fapi/v1/ticker/bookTicker

    https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

    Note:
       If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    Keyword Args:
        symbol (str): the trading pair
    """
    params = {"symbol": symbol}
    return self.query("/fapi/v1/ticker/bookTicker", params)


def open_interest(self, symbol: str):
    """Open Interest
    Get present open interest of a specific symbol.


    GET /fapi/v1/openInterest

    https://binance-docs.github.io/apidocs/futures/en/#open-interest

    Args:
       symbol (str): the trading pair.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol}
    return self.query("/fapi/v1/openInterest", params)


def open_interest_statistics(self, symbol: str, period: str, **kwargs):
    """Open Interest Statistics
    Get present open interest statistics of a specific symbol.


    GET /futures/data/openInterestHist

    https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics

    Args:
       symbol (str): the trading pair.
       period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d".
    Keyword Args:
        limit (int, optional)
        startTime (int, optional)
        endTime (int, optional)
    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/openInterestHist", params)


def top_trader_accounts(self, symbol: str, period: str, **kwargs):
    """Top Trader Long/Short Ratio (Accounts) (MARKET_DATA)
    GET /futures/data/topLongShortAccountRatio

    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-accounts-market_data

    Args:
       symbol (str): the trading pair.
       period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d"
    Keyword Args:
       startTime (int, optional): Timestamp in ms from INCLUSIVE.
       endTime (int, optional): Timestamp in ms until INCLUSIVE.
       limit (int, optional): limit the results. Default 30; max 500.

    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortAccountRatio", params)


def top_trader_positions(self, symbol: str, period: str, **kwargs):
    """Top Trader Long/Short Ratio (Accounts) (MARKET_DATA)

    GET /futures/data/topLongShortPositionRatio

    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions

    Args:
       symbol (str): the trading pair.
       period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d"
    Keyword Args:
       startTime (int, optional): Timestamp in ms from INCLUSIVE.
       endTime (int, optional): Timestamp in ms until INCLUSIVE.
       limit (int, optional): limit the results. Default 30; max 500.

    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortPositionRatio", params)


def ratio(self, symbol: str, period: str, **kwargs):
    """Top Trader Long/Short Ratio (Positions)

    GET /futures/data/globalLongShortAccountRatio

    https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio

    Args:
       symbol (str): the trading pair.
       period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d"
    Keyword Args:
       startTime (int, optional): Timestamp in ms from INCLUSIVE.
       endTime (int, optional): Timestamp in ms until INCLUSIVE.
       limit (int, optional): limit the results. Default 30; max 500.

    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/globalLongShortAccountRatio", params)


def taker_volume(self, symbol: str, period: str, **kwargs):
    """Taker Buy/Sell Volume
    GET /futures/data/takerlongshortRatio

    https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume

    Args:
       symbol (str): the trading pair.
       period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d"
    Keyword Args:
       startTime (int, optional): Timestamp in ms from INCLUSIVE.
       endTime (int, optional): Timestamp in ms until INCLUSIVE.
       limit (int, optional): limit the results. Default 30; max 500.

    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/takerlongshortRatio", params)


def historical_blvt_nav_kline(self, symbol: str, interval: str, **kwargs):
    """Historical BLVT NAV Kline/Candlestick
    The BLVT NAV system is based on Binance Futures, so the endpoint is based on fapi


    GET /fapi/v1/lvtKlines

    https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick

    Args:
       symbol (str): the trading pair, eg: BTCDOWN.
       interval (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d"
    Keyword Args:
       startTime (int, optional): Timestamp in ms from INCLUSIVE.
       endTime (int, optional): Timestamp in ms until INCLUSIVE.
       limit (int, optional): limit the results. Default 500; max 1000.

    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/lvtKlines", params)


def composite_index(self, symbol: str = None):
    """Composite Index Symbol Information
    Only for composite index symbols

    GET /fapi/v1/indexInfo

    https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information

    Args:
       symbol (str): the trading pair, eg: DEFIUSDT.

    """
    params = {"symbol": symbol}
    return self.query("/fapi/v1/indexInfo", params)
