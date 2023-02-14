from binance.lib.utils import get_uuid, purge_map, websocket_api_signature


def account(self, **kwargs):
    """Account information (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        recvWindow (int, optional): The value cannot be greater than 60000

    Message sent:

    .. code-block:: json

        {
            "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",
            "method": "account.status",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "83303b4a136ac1371795f465808367242685a9e3a42b22edb4d977d0696eb45c",
                "timestamp": 1660801839480
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",
            "status": 200,
            "result": {
                "makerCommission": 15,
                "takerCommission": 15,
                "buyerCommission": 0,
                "sellerCommission": 0,
                "canTrade": true,
                "canWithdraw": true,
                "canDeposit": true,
                "commissionRates": {
                    "maker": "0.00150000",
                    "taker": "0.00150000",
                    "buyer": "0.00000000",
                    "seller":"0.00000000"
                },
                "brokered": false,
                "requireSelfTradePrevention": false,
                "updateTime": 1660801833000,
                "accountType": "SPOT",
                "balances": [
                    {
                        "asset": "BNB",
                        "free": "0.00000000",
                        "locked": "0.00000000"
                    },
                    {
                        "asset": "BTC",
                        "free": "1.3447112",
                        "locked": "0.08600000"
                    },
                    {
                        "asset": "USDT",
                        "free": "1021.21000000",
                        "locked": "0.00000000"
                    }
                ],
                "permissions": [
                    "SPOT"
                ]
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 10
                }
            ]
        }

    """

    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "account.status",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def order_rate_limit(self, **kwargs):
    """Account order rate limits (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        recvWindow (int, optional): The value cannot be greater than 60000

    Message sent:

    .. code-block:: json

        {
            "id": "d3783d8d-f8d1-4d2c-b8a0-b7596af5a664",
            "method": "account.rateLimits.orders",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "76289424d6e288f4dc47d167ac824e859dabf78736f4348abbbac848d719eb94",
                "timestamp": 1660801839500
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "d3783d8d-f8d1-4d2c-b8a0-b7596af5a664",
            "status": 200,
            "result": [{
                "rateLimitType": "ORDERS",
                "interval": "SECOND",
                "intervalNum": 1,
                "limit": 200
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "DAY",
                "intervalNum": 1,
                "limit": 100000
            }],
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }

    """

    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "account.rateLimits.orders",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def order_history(self, **kwargs):
    """Account order history (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        symbol (str, optional): Symbol
        orderId (int, optional): Order ID
        startTime (int, optional): Timestamp in ms
        endTime (int, optional): Timestamp in ms
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000

    Message sent:

    .. code-block:: json

        {
            "id": "734235c2-13d2-4574-be68-723e818c08f3",
            "method": "allOrders",
            "params": {
                "symbol": "BTCUSDT",
                "startTime": 1660780800000,
                "endTime": 1660867200000,
                "limit": 5,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "f50a972ba7fad92842187643f6b930802d4e20bce1ba1e788e856e811577bd42",
                "timestamp": 1661955123341
            }
        }


    Response

    .. code-block:: json

        {
            "id": "734235c2-13d2-4574-be68-723e818c08f3",
            "status": 200,
            "result": [{
                "symbol": "BTCUSDT",
                "orderId": 12569099453,
                "orderListId": -1,
                "clientOrderId": "4d96324ff9d44481926157",
                "price": "23416.10000000",
                "origQty": "0.00847000",
                "executedQty": "0.00847000",
                "cummulativeQuoteQty": "198.33521500",
                "status": "FILLED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "stopPrice": "0.00000000",
                "icebergQty": "0.00000000",
                "time": 1660801715639,
                "updateTime": 1660801717945,
                "isWorking": true,
                "workingTime": 1660801715639,
                "origQuoteOrderQty": "0.00000000",
                "selfTradePreventionMode": "NONE",
                "preventedMatchId": 0,
                "preventedQuantity": "1.200000"
                }],
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }

    """

    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "allOrders",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def oco_history(self, **kwargs):
    """Account OCO history (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        fromId (int, optional): OCO ID
        startTime (int, optional): Timestamp in ms
        endTime (int, optional): Timestamp in ms
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000

    Message sent:

    .. code-block:: json

        {
            "id": "8617b7b3-1b3d-4dec-94cd-eefd929b8ceb",
            "method": "allOrderLists",
            "params": {
                "startTime": 1660780800000,
                "endTime": 1660867200000,
                "limit": 5,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "c8e1484db4a4a02d0e84dfa627eb9b8298f07ebf12fcc4eaf86e4a565b2712c2",
                "timestamp": 1661955123341
            }
        }


    Response

    .. code-block:: json

        {
            "id": "8617b7b3-1b3d-4dec-94cd-eefd929b8ceb",
            "status": 200,
            "result": [{
                "orderListId": 1274512,
                "contingencyType": "OCO",
                "listStatusType": "EXEC_STARTED",
                "listOrderStatus": "EXECUTING",
                "listClientOrderId": "08985fedd9ea2cf6b28996",
                "transactionTime": 1660801713793,
                "symbol": "BTCUSDT",
                "orders": [{
                    "symbol": "BTCUSDT",
                    "orderId": 12569138901,
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569138902,
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
                }]
            }],
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }

    """

    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "allOrderLists",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def my_trades(self, **kwargs):
    """Account trade history (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        symbol (str, optional): Symbol
        orderId (int, optional): order id
        startTime (int, optional): Timestamp in ms
        endTime (int, optional): Timestamp in ms
        fromId (int, optional): Trade id to fetch from. Default gets most recent trades.
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000

    Message sent:

    .. code-block:: json

        {
            "id": "f4ce6a53-a29d-4f70-823b-4ab59391d6e8",
            "method": "myTrades",
            "params": {
                "symbol": "BTCUSDT",
                "startTime": 1660780800000,
                "endTime": 1660867200000,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
                "timestamp": 1661955125250
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "f4ce6a53-a29d-4f70-823b-4ab59391d6e8",
            "status": 200,
            "result": [
                {
                    "symbol": "BTCUSDT",
                    "id": 12569138901,
                    "orderId": 12569138901,
                    "price": "0.00000000",
                    "qty": "0.00000000",
                    "commission": "0.00000000",
                    "commissionAsset": "BTC",
                    "time": 1660801715639,
                    "isBuyer": true,
                    "isMaker": false,
                    "isBestMatch": true
                }
            ],
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }

    """

    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "myTrades",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def prevented_matches(self, symbol: str, **kwargs):
    """Account prevented matches (USER_DATA)

    Keyword Args:
        id (str, optional): Client generated ID.
        symbol (str, optional): Symbol
        preventedMatchId (int, optional): Prevented match id
        orderId (int, optional): order id
        fromPrevMatchId (int, optional): Prevented match id to fetch from.
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000


    Combinations supported::
      - symbol + preventedMatchId
      - symbol + orderId
      - symbol + orderId + fromPreventedMatchId (limit will default to 500)
      - symbol + orderId + fromPreventedMatchId + limit


    Message sent:

    .. code-block:: json

        {
            "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
            "method": "myPreventedMatches",
            "params": {
                "symbol": "BTCUSDT",
                "orderId": 35,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
                "timestamp": 1673923281052
            }
        }


    Response

    .. code-block:: json

        {
            "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
            "status": 200,
            "result": [{
                "symbol": "BTCUSDT",
                "preventedMatchId": 1,
                "takerOrderId": 5,
                "makerOrderId": 3,
                "tradeGroupId": 1,
                "selfTradePreventionMode": "EXPIRE_MAKER",
                "price": "1.100000",
                "makerPreventedQuantity": "1.300000",
                "transactTime": 1669101687094
            }],
            "rateLimits": [{
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 10
            }]
        }

    """
    parameters = {"symbol": symbol, **kwargs}
    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "myPreventedMatches",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)
