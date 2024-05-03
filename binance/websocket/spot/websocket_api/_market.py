from binance.lib.utils import get_uuid, purge_map
from binance.error import ParameterArgumentError


def ping_connectivity(self, id=None):
    """Test connectivity to the WebSocket API.

    Args:
        id (str): request id

    Message sent:

    .. code-block:: json

        {
            "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",
            "method": "ping"
        }


    Response:

    .. code-block:: json

        {
            "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",
            "status": 200,
            "result": {},
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
            }]
        }


    Note: You can use regular WebSocket ping frames to test connectivity as well,
    WebSocket API will respond with pong frames as soon as possible.

    """

    if not id:
        id = get_uuid()

    payload = {"id": id, "method": "ping"}

    self.send(payload)


def server_time(self, id=None):
    """Check server time

    Args:
        id (str): request id

    Message sent:

    .. code-block:: json

        {
            "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
            "method": "time"
        }


    Response:

    .. code-block:: json

        {
            "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
            "status": 200,
            "result": {
                "serverTime": 1656400526260
            },
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
            }]
        }


    Test connectivity to the WebSocket API and get the current server time.

    """

    if not id:
        id = get_uuid()

    payload = {"id": id, "method": "time"}

    self.send(payload)


def exchange_info(self, **kwargs):
    """Exchange information

    Query current exchange trading rules, rate limits, and symbol information.

    Note: For symbol, Upper case is required.

    Keyword Args:
        symbols (list): symbols to get info
        symbol (str): symbol to get info
        permissons (list): permissions to get info

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "exchangeInfo",
            "params": {
                "symbols": [
                    "BNBBTC"
                ]
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
            "timezone": "UTC",
            "serverTime": 1655969291181,
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "SECOND",
                "intervalNum": 10,
                "limit": 50
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "DAY",
                "intervalNum": 1,
                "limit": 160000
            },
            {
                "rateLimitType": "RAW_REQUESTS",
                "interval": "MINUTE",
                "intervalNum": 5,
                "limit": 6100
            }],
            "exchangeFilters": [],
            "symbols": [{
                "symbol": "BNBBTC",
                "status": "TRADING",
                "baseAsset": "BNB",
                "baseAssetPrecision": 8,
                "quoteAsset": "BTC",
                "quotePrecision": 8,
                "quoteAssetPrecision": 8,
                "baseCommissionPrecision": 8,
                "quoteCommissionPrecision": 8,
                "orderTypes": [
                    "LIMIT",
                    "LIMIT_MAKER",
                    "MARKET",
                    "STOP_LOSS_LIMIT",
                    "TAKE_PROFIT_LIMIT"
                ],
                "icebergAllowed": true,
                "ocoAllowed": true,
                "quoteOrderQtyMarketAllowed": true,
                "allowTrailingStop": true,
                "cancelReplaceAllowed": true,
                "isSpotTradingAllowed": true,
                "isMarginTradingAllowed": true,
                "filters": [{
                    "filterType": "PRICE_FILTER",
                    "minPrice": "0.00000100",
                    "maxPrice": "100000.00000000",
                    "tickSize": "0.00000100"
                },
                {
                    "filterType": "LOT_SIZE",
                    "minQty": "0.00100000",
                    "maxQty": "100000.00000000",
                    "stepSize": "0.00100000"
                }],
                "permissions": [
                    "SPOT",
                    "MARGIN",
                    "TRD_GRP_004"
                ],
                "defaultSelfTradePreventionMode": "NONE",
                "allowedSelfTradePreventionModes": [
                    "NONE"
                ]
            }]},
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }
    """
    parameters = {**kwargs}

    parameters = purge_map(parameters)

    if len(parameters) > 1:
        raise ParameterArgumentError(
            "Only one of symbol, symbols or permissions is required."
        )

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "exchangeInfo",
        "params": parameters,
    }

    self.send(payload)


def order_book(self, symbol: str, **kwargs):
    """Order book

    Args:
        symbol (str): symbol to get order book

    Keyword Args:
        limit (int): limit of order book

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "depth",
            "params": {
                "symbol": "BNBBTC",
                "limit": 10
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
                "lastUpdateId": 2731179239,
                "bids": [
                    [
                        "0.01379900",
                        "3.43200000"
                    ],
                    [
                        "0.01379800",
                        "3.24300000"
                    ],
                    [
                        "0.01379700",
                        "10.45500000"
                    ],
                    [
                        "0.01379600",
                        "3.82100000"
                    ],
                    [
                        "0.01379500",
                        "10.26200000"
                    ]
                ],
                "asks": [
                    [
                        "0.01380000",
                        "5.91700000"
                    ],
                    [
                        "0.01380100",
                        "6.01400000"
                    ],
                    [
                        "0.01380200",
                        "0.26800000"
                    ],
                    [
                        "0.01380300",
                        "0.33800000"
                    ],
                    [
                        "0.01380400",
                        "0.26800000"
                    ]
                ]
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }
    """
    parameters = {"symbol": symbol.upper(), **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "depth",
        "params": parameters,
    }

    self.send(payload)


def recent_trades(self, symbol: str, **kwargs):
    """Recent trades

    Args:
        symbol (str): symbol to get recent trades

    Keyword Args:
        limit (int): limit of recent trades

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "trades.recent",
            "params": {
                "symbol": "BNBBTC",
                "limit": 10
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": [
                {
                    "id": 194686783,
                    "price": "0.01361000",
                    "qty": "0.01400000",
                    "quoteQty": "0.00019054",
                    "time": 1660009530807,
                    "isBuyerMaker": true,
                    "isBestMatch": true
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }
    """

    parameters = {"symbol": symbol.upper(), **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "trades.recent",
        "params": parameters,
    }

    self.send(payload)


def historical_trades(self, symbol: str, apiKey: str, **kwargs):
    """Historical trades

    Args:
        symbol (str): symbol to get historical trades

    Keyword Args:
        symbol (str): symbol to get historical trades
        fromId (int): trade id to fetch from
        limit (int): limit of historical trades

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "trades.historical",
            "params": {
                "symbol": "BNBBTC",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "fromId": 0,
                "limit": 1
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": [
                {
                    "id": 0,
                    "price": "0.01361000",
                    "qty": "0.01400000",
                    "quoteQty": "0.00019054",
                    "time": 1660009530807,
                    "isBuyerMaker": true,
                    "isBestMatch": true
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }
    """
    parameters = {"symbol": symbol.upper(), "apiKey": apiKey, **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "trades.historical",
        "params": parameters,
    }

    self.send(payload)


def aggregate_trades(self, symbol: str, **kwargs):
    """Aggregate trades

    Args:
        symbol (str): symbol to get aggregate trades

    Keyword Args:
        symbol (str): symbol to get aggregate trades
        fromId (int): trade id to fetch from
        limit (int): limit of aggregate trades
        startTime (int): start time to fetch from
        endTime (int): end time to fetch from

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "trades.aggregate",
            "params": {
                "symbol": "BNBBTC",
                "fromId": 0,
                "limit": 1
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": [
                {
                    "a": 0,
                    "p": "0.01361000",
                    "q": "0.01400000",
                    "f": 0,
                    "l": 0,
                    "T": 1660009530807,
                    "m": true,
                    "M": true
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = {"symbol": symbol.upper(), **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "trades.aggregate",
        "params": parameters,
    }

    self.send(payload)


def klines(self, symbol: str, interval: str, **kwargs):
    """Klines/candlesticks

    Args:
        symbol (str): symbol to get klines
        interval (str): interval of klines

    Keyword Args:
        startTime (int): start time to fetch from
        endTime (int): end time to fetch from
        limit (int): limit of klines

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "klines",
            "params": {
                "symbol": "BNBBTC",
                "interval": "1m",
                "startTime": 1655969280000,
                "limit": 1
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": [
                [
                    1660009530807,
                    "0.01361000",
                    "0.01361000",
                    "0.01361000",
                    "0.01361000",
                    "0.01400000",
                    1660009530807,
                    "0.00019054",
                    0,
                    "0.00000000",
                    "0.00000000",
                    "0"
                ]
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = {"symbol": symbol.upper(), "interval": interval, **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "klines",
        "params": parameters,
    }

    self.send(payload)


def ui_klines(self, symbol: str, interval: str, **kwargs):
    """Klines/candlesticks for UI

    Args:
        symbol (str): symbol to get klines
        interval (str): interval of klines

    Keyword Args:
        startTime (int): start time to fetch from
        endTime (int): end time to fetch from
        limit (int): limit of klines

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "uiKlines",
            "params": {
                "symbol": "BNBBTC",
                "interval": "1m",
                "startTime": 1655969280000,
                "limit": 1
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": [
                [
                    1660009530807,
                    "0.01361000",
                    "0.01361000",
                    "0.01361000",
                    "0.01361000",
                    "0.01400000",
                    1660009530807,
                    "0.00019054",
                    0,
                    "0.00000000",
                    "0.00000000",
                    "0"
                ]
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = {"symbol": symbol.upper(), "interval": interval, **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "uiKlines",
        "params": parameters,
    }

    self.send(payload)


def avg_price(self, symbol: str, **kwargs):
    """Current average price for a symbol

    Args:
        symbol (str): symbol to get average price

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "avgPrice",
            "params": {
                "symbol": "BNBBTC"
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
                "mins": 5,
                "price": "0.01361000"
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = {"symbol": symbol.upper(), **kwargs}

    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "avgPrice",
        "params": parameters,
    }

    self.send(payload)


def ticker_24hr(self, **kwargs):
    """24 hour rolling window price change statistics

    Keyword Args:
        symbol (str): symbol to get ticker 24hr
        symbols (list): symbols to get ticker 24hr
        type (str): type of ticker 24hr

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "ticker.24hr",
            "params": {
                "symbol": "BNBBTC"
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
                "symbol": "BNBBTC",
                "priceChange": "-94.99999800",
                "priceChangePercent": "-95.960",
                "weightedAvgPrice": "0.29628482",
                "prevClosePrice": "0.10002000",
                "lastPrice": "4.00000200",
                "lastQty": "200.00000000",
                "bidPrice": "4.00000000",
                "bidQty": "10.00000000",
                "askPrice": "4.00000200",
                "askQty": "10.00000000",
                "openPrice": "99.00000000",
                "highPrice": "100.00000000",
                "lowPrice": "0.10000000",
                "volume": "8913.30000000",
                "quoteVolume": "15.30000000",
                "openTime": 1499783499040,
                "closeTime": 1499869899040,
                "firstId": 28385,
                "lastId": 28460,
                "count": 76
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "ticker.24hr",
        "params": parameters,
    }

    self.send(payload)


def ticker(self, **kwargs):
    """Rolling window price change statistics

    Keyword Args:
        symbol (str): symbol to get ticker
        symbols (list): symbols to get ticker
        type (str): type of ticker
        windowSize (str): window size of ticker

    Message sent:

    .. code-block:: json

        {
            "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
            "method": "ticker",
            "params": {
                "symbols": [
                    "BNBBTC",
                    "BTCUSDT"
                ],
                "windowSize": "7d"
            }
        }


    Response

    .. code-block:: json

        {
            "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
            "status": 200,
            "result": {
                "symbol": "BNBBTC",
                "priceChange": "0.00061500",
                "priceChangePercent": "4.735",
                "weightedAvgPrice": "0.01368242",
                "openPrice": "0.01298900",
                "highPrice": "0.01418800",
                "lowPrice": "0.01296000",
                "lastPrice": "0.01360400",
                "volume": "587179.23900000",
                "quoteVolume": "8034.03382165",
                "openTime": 1659580020000,
                "closeTime": 1660184865291,
                "firstId": 192977765,
                "lastId": 195365758,
                "count": 2387994
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 2
                }
            ]
        }

    """
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "ticker",
        "params": parameters,
    }

    self.send(payload)


def ticker_price(self, **kwargs):
    """Symbol price ticker

    Keyword Args:
        symbol (str): symbol to get ticker price
        symbols (list): symbols to get ticker price

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "ticker.price",
            "params": {
                "symbol": "BNBBTC"
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
                "symbol": "BNBBTC",
                "price": "4.00000200"
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "ticker.price",
        "params": parameters,
    }

    self.send(payload)


def ticker_book(self, **kwargs):
    """Symbol order book ticker

    Keyword Args:
        symbol (str): symbol to get ticker book
        symbols (list): symbols to get ticker book

    Message sent:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "method": "ticker.book",
            "params": {
                "symbol": "BNBBTC"
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5494febb-d167-46a2-996d-70533eb4d976",
            "status": 200,
            "result": {
                "symbol": "BNBBTC",
                "bidPrice": "4.00000000",
                "bidQty": "431.00000000",
                "askPrice": "4.00000200",
                "askQty": "9.00000000"
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

    """
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "ticker.book",
        "params": parameters,
    }

    self.send(payload)
