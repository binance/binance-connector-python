from binance.lib.utils import get_uuid, purge_map, websocket_api_signature


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """Create a new order.

    Args:
        symbol (str): Symbol to trade.
        side (str): Side of the trade.
        type (str): Type of the trade.
    Keyword Args:
        timeInForce (str): Time in force.
        quantity (float): Quantity of the trade.
        quoteOrderQty (float): Quote order quantity.
        price (float): Price of the trade.
        newClientOrderId (str): New client order id.
        stopPrice (float): Stop price.
        trailingDelta (int): Trailing delta.
        icebergQty (float): Iceberg quantity.
        strategyId (int): Strategy id.
        strategyType (int): Strategy type.
        selfTradePreventionMode (str): Self trade prevention.
        newOrderRespType (str): New order response type.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "56374a46-3061-486b-a311-99ee972eb648",
            "method": "order.place",
            "params": {
                "symbol": "BTCUSDT",
                "side": "SELL",
                "type": "LIMIT",
                "timeInForce": "GTC",
                "price": "23416.10000000",
                "quantity": "0.00847000",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
                "timestamp": 1660801715431
            }
        }



    Response

    .. code-block:: json

        {
            "id": "56374a46-3061-486b-a311-99ee972eb648",
            "status": 200,
            "result": {
                "symbol": "BTCUSDT",
                "orderId": 12569099453,
                "orderListId": -1,
                "clientOrderId": "4d96324ff9d44481926157ec08158a40",
                "transactTime": 1660801715639
            },
            "rateLimits": [
                {
                    "rateLimitType": "ORDERS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 50,
                    "count": 1
                },
                {
                    "rateLimitType": "ORDERS",
                    "interval": "DAY",
                    "intervalNum": 1,
                    "limit": 160000,
                    "count": 1
                },
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

    parameters = {"symbol": symbol, "side": side, "type": type, **kwargs}
    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "order.place",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def new_order_test(self, symbol: str, side: str, type: str, **kwargs):
    """Test new order (TRADE)

    Args:
        symbol (str): Symbol to trade.
        side (str): Side of the trade.
        type (str): Type of the trade.
    Keyword Args:
        timeInForce (str): Time in force.
        quantity (float): Quantity of the trade.
        quoteOrderQty (float): Quote order quantity.
        price (float): Price of the trade.
        newClientOrderId (str): New client order id.
        stopPrice (float): Stop price.
        trailingDelta (int): Trailing delta.
        icebergQty (float): Iceberg quantity.
        strategyId (int): Strategy id.
        strategyType (int): Strategy type.
        selfTradePreventionMode (str): Self trade prevention.
        newOrderRespType (str): New order response type.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "56374a46-3061-486b-a311-99ee972eb648",
            "method": "order.test",
            "params": {
                "symbol": "BTCUSDT",
                "side": "SELL",
                "type": "LIMIT",
                "timeInForce": "GTC",
                "price": "23416.10000000",
                "quantity": "0.00847000",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
                "timestamp": 1660801715431
            }
        }



    Response

    .. code-block:: json

        {
            "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",
            "status": 200,
            "result": {},
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

    parameters = {"symbol": symbol, "side": side, "type": type, **kwargs}
    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "order.test",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def get_order(self, symbol: str, **kwargs):
    """Get order (USER_DATA)

    Args:
        symbol (str): Symbol to trade.
    Keyword Args:
        orderId (int): Order id.
        origClientOrderId (str): Original client order id.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",
            "method": "order.status",
            "params": {
                "symbol": "BTCUSDT",
                "orderId": 12569099453,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "2c3aab5a078ee4ea465ecd95523b77289f61476c2f238ec10c55ea6cb11a6f35",
                "timestamp": 1660801720951
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",
            "status": 200,
            "result": {
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
                "trailingDelta": 10,
                "trailingTime": -1,
                "icebergQty": "0.00000000",
                "time": 1660801715639,
                "updateTime": 1660801717945,
                "isWorking": true,
                "workingTime": 1660801715639,
                "origQuoteOrderQty": "0.00000000",
                "strategyId": 37463720,
                "strategyType": 1000000,
                "selfTradePreventionMode": "NONE",
                "preventedMatchId": 0,
                "preventedQuantity": "1.200000"
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

    parameters = {"symbol": symbol, **kwargs}
    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "order.status",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def cancel_order(self, symbol: str, **kwargs):
    """Cancel order (USER_DATA)
      Args:
        symbol (str): Symbol to trade.
      Keyword Args:
        orderId (int): Order id.
        origClientOrderId (str): Original client order id.
        newClientOrderId (str): New client order id.
        recvWindow (int): Recv window.

      Message sent:

    .. code-block:: json

        {
            "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",
            "method": "order.cancel",
            "params": {
                "symbol": "BTCUSDT",
                "origClientOrderId": "4d96324ff9d44481926157",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "33d5b721f278ae17a52f004a82a6f68a70c68e7dd6776ed0be77a455ab855282",
                "timestamp": 1660801715830
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",
            "status": 200,
            "result": {
                "symbol": "BTCUSDT",
                "origClientOrderId": "4d96324ff9d44481926157",
                "orderId": 12569099453,
                "orderListId": -1,
                "clientOrderId": "91fe37ce9e69c90d6358c0",
                "price": "23416.10000000",
                "origQty": "0.00847000",
                "executedQty": "0.00001000",
                "cummulativeQuoteQty": "0.23416100",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "stopPrice": "0.00000000",
                "trailingDelta": 0,
                "trailingTime": -1,
                "icebergQty": "0.00000000",
                "strategyId": 37463720,
                "strategyType": 1000000,
                "selfTradePreventionMode": "NONE"
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

    parameters = {"symbol": symbol, **kwargs}
    parameters = purge_map(parameters)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "order.cancel",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }

    self.send(payload)


def cancel_replace_order(
    self, symbol: str, cancelReplaceMode: str, side: str, type: str, **kwargs
):
    """Cancel and replace order
    Args:
        symbol (str): Symbol to trade.
        cancelReplaceMode (str):
        side (str): SIDE
        type (str): ORDER_TYPE
    Keyword Args:
        cancelOrderId (int): Cancel order by orderId
        cancelOrigClientOrderId (int): Cancel order by clientOrderId.
        cancelNewClientOrderId (str): New ID for the canceled order. Automatically generated if not sent
        timeInForce (str): Time in force.
        price (float): Price.
        quantity (float): Quantity.
        quoteOrderQty (float): Quote order quantity.
        newClientOrderId (str): New client order id.
        newOrderRespType (str): New order response type.
        stopPrice (float): Stop price.
        trailingDelta (float): Trailing delta.
        icebergQty (float): Iceberg quantity.
        strategyId (int): Strategy id.
        strategyType (int): Strategy type.
        selfTradePreventionMode (str): Self trade prevention mode.
        recvWindow (int): Recv window.

    Message Sent:

    .. code-block:: json

        {
            "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",
            "method": "order.cancelReplace",
            "params": {
                "symbol": "BTCUSDT",
                "cancelReplaceMode": "ALLOW_FAILURE",
                "cancelOrigClientOrderId": "4d96324ff9d44481926157",
                "side": "SELL",
                "type": "LIMIT",
                "timeInForce": "GTC",
                "price": "23416.10000000",
                "quantity": "0.00847000",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "7028fdc187868754d25e42c37ccfa5ba2bab1d180ad55d4c3a7e2de643943dc5",
                "timestamp": 1660813156900
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "b220edfe-f3c4-4a3a-9d13-b35473783a25",
            "status": 409,
            "error": {
                "code": -2021,
                "msg": "Order cancel-replace partially failed.",
                "data": {
                "cancelResult": "SUCCESS",
                "newOrderResult": "FAILURE",
                "cancelResponse": {
                    "symbol": "BTCUSDT",
                    "origClientOrderId": "4d96324ff9d44481926157",
                    "orderId": 125690984230,
                    "orderListId": -1,
                    "clientOrderId": "91fe37ce9e69c90d6358c0",
                    "price": "23450.00000000",
                    "origQty": "0.00847000",
                    "executedQty": "0.00001000",
                    "cummulativeQuoteQty": "0.23450000",
                    "status": "CANCELED",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "side": "SELL",
                    "selfTradePreventionMode": "NONE"
                },
                "newOrderResponse": {
                    "code": -2010,
                    "msg": "Order would immediately match and take."
                }
                }
            },
            "rateLimits": [
                {
                    "rateLimitType": "ORDERS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 50,
                    "count": 1
                },
                {
                    "rateLimitType": "ORDERS",
                    "interval": "DAY",
                    "intervalNum": 1,
                    "limit": 160000,
                    "count": 1
                },
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 1
                }
            ]
        }

        {
            "id": "ce641763-ff74-41ac-b9f7-db7cbe5e93b1",
            "status": 409,
            "error": {
                "code": -2021,
                "msg": "Order cancel-replace partially failed.",
                "data": {
                "cancelResult": "FAILURE",
                "newOrderResult": "SUCCESS",
                "cancelResponse": {
                    "code": -2011,
                    "msg": "Unknown order sent."
                },
                "newOrderResponse": {
                    "symbol": "BTCUSDT",
                    "orderId": 12569099453,
                    "orderListId": -1,
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",
                    "transactTime": 1660813156959,
                    "price": "23416.10000000",
                    "origQty": "0.00847000",
                    "executedQty": "0.00000000",
                    "cummulativeQuoteQty": "0.00000000",
                    "status": "NEW",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "side": "SELL",
                    "workingTime": 1669693344508,
                    "fills": [],
                    "selfTradePreventionMode": "NONE"
                }
                }
            },
            "rateLimits": [
                {
                    "rateLimitType": "ORDERS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 50,
                    "count": 1
                },
                {
                    "rateLimitType": "ORDERS",
                    "interval": "DAY",
                    "intervalNum": 1,
                    "limit": 160000,
                    "count": 1
                },
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

    parameters = {
        "symbol": symbol,
        "cancelReplaceMode": cancelReplaceMode,
        "side": side,
        "type": type,
        **kwargs,
    }
    parameters = purge_map(parameters)
    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "order.cancelReplace",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def get_open_orders(self, **kwargs):
    """Current open orders (USER_DATA)

    Keyword Arguments:
        symbol (str): Symbol.
        recvWindow (int): Recv window.

    Message Sent:

    .. code-block:: json

        {
            "id": "55f07876-4f6f-4c47-87dc-43e5fff3f2e7",
            "method": "openOrders.status",
            "params": {
                "symbol": "BTCUSDT",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "d632b3fdb8a81dd44f82c7c901833309dd714fe508772a89b0a35b0ee0c48b89",
                "timestamp": 1660813156812
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "55f07876-4f6f-4c47-87dc-43e5fff3f2e7",
            "status": 200,
            "result": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569099453,
                    "orderListId": -1,
                    "clientOrderId": "4d96324ff9d44481926157",
                    "price": "23416.10000000",
                    "origQty": "0.00847000",
                    "executedQty": "0.00720000",
                    "cummulativeQuoteQty": "172.43931000",
                    "status": "PARTIALLY_FILLED",
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
                    "selfTradePreventionMode": "NONE"
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 3
                }
            ]
        }

    """

    parameters = purge_map(kwargs)
    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "openOrders.status",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def cancel_open_orders(self, symbol: str, **kwargs):
    """Cancel all open orders on a symbol (USER_DATA)

    Arguments:
        symbol (str): Symbol.
    Keyword Arguments:
        recvWindow (int): Recv window.

    Message Sent:

    .. code-block:: json

        {
            "id": "778f938f-9041-4b88-9914-efbf64eeacc8",
            "method": "openOrders.cancelAll"
            "params": {
                "symbol": "BTCUSDT",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "773f01b6e3c2c9e0c1d217bc043ce383c1ddd6f0e25f8d6070f2b66a6ceaf3a5",
                "timestamp": 1660805557200
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "778f938f-9041-4b88-9914-efbf64eeacc8",
            "status": 200,
            "result": [
                {
                    "symbol": "BTCUSDT",
                    "origClientOrderId": "4d96324ff9d44481926157",
                    "orderId": 12569099453,
                    "orderListId": -1,
                    "clientOrderId": "91fe37ce9e69c90d6358c0",
                    "price": "23416.10000000",
                    "origQty": "0.00847000",
                    "executedQty": "0.00001000",
                    "cummulativeQuoteQty": "0.23416100",
                    "status": "CANCELED",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "side": "SELL",
                    "stopPrice": "0.00000000",
                    "trailingDelta": 0,
                    "trailingTime": -1,
                    "icebergQty": "0.00000000",
                    "strategyId": 37463720,
                    "strategyType": 1000000,
                    "selfTradePreventionMode": "NONE"
                },
                {
                    "orderListId": 19431,
                    "contingencyType": "OCO",
                    "listStatusType": "ALL_DONE",
                    "listOrderStatus": "ALL_DONE",
                    "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",
                    "transactionTime": 1660803702431,
                    "symbol": "BTCUSDT",
                    "orders": [
                        {
                        "symbol": "BTCUSDT",
                        "orderId": 12569099453,
                        "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"
                        },
                        {
                        "symbol": "BTCUSDT",
                        "orderId": 12569099454,
                        "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"
                        }
                    ],
                    "orderReports": [
                        {
                            "symbol": "BTCUSDT",
                            "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",
                            "orderId": 12569099453,
                            "orderListId": 19431,
                            "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                            "price": "23450.50000000",
                            "origQty": "0.00850000",
                            "executedQty": "0.00000000",
                            "cummulativeQuoteQty": "0.00000000",
                            "status": "CANCELED",
                            "timeInForce": "GTC",
                            "type": "STOP_LOSS_LIMIT",
                            "side": "BUY",
                            "stopPrice": "23430.00000000",
                            "selfTradePreventionMode": "NONE"
                        },
                        {
                            "symbol": "BTCUSDT",
                            "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",
                            "orderId": 12569099454,
                            "orderListId": 19431,
                            "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                            "price": "23400.00000000",
                            "origQty": "0.00850000",
                            "executedQty": "0.00000000",
                            "cummulativeQuoteQty": "0.00000000",
                            "status": "CANCELED",
                            "timeInForce": "GTC",
                            "type": "LIMIT_MAKER",
                            "side": "BUY",
                            "selfTradePreventionMode": "NONE"
                        }
                    ]
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

    parameters = purge_map({"symbol": symbol, **kwargs})
    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "openOrders.cancelAll",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def new_oco_order(self, symbol: str, side: str, price, quantity, **kwargs):
    """Place a new OCO Order (TRADE)
    Args:
        symbol (str): Symbol.
        side (str): BUY or SELL.
        price (float): Price.
        quantity (float): Quantity.
    Keyword Arguments:
        listClientOrderId (str): A unique id for the entire order list.
        limitClientOrderId (str): A unique id for the limit order.
        limitIcebergQty (float): Iceberg quantity.
        limitStrategyId (int): Strategy id.
        limitStrategyType (int): Strategy type.
        stopPrice (float): Stop price.
        trailingDelta (float): Trailing delta.
        stopClientOrderId (str): A unique id for the stop loss order.
        stopLimitPrice (float): Stop limit price.
        stopLimitTimeInForce (str): GTC or FOK.
        stopIcebergQty (float): Iceberg quantity.
        stopStrategyId (int): Strategy id.
        stopStrategyType (int): Strategy type.
        newOrderRespType (str): ACK, RESULT, or FULL; MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        selfTradePreventionMode (str): NONE, EXPIRE_TAKER, EXPIRE_MAKER or EXPIRE_BOTH.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "56374a46-3061-486b-a311-99ee972eb648",
            "method": "orderList.place",
            "params": {
                "symbol": "BTCUSDT",
                "side": "SELL",
                "price": "23420.00000000",
                "quantity": "0.00650000",
                "stopPrice": "23410.00000000",
                "stopLimitPrice": "23405.00000000",
                "stopLimitTimeInForce": "GTC",
                "newOrderRespType": "RESULT",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "6689c2a36a639ff3915c2904871709990ab65f3c7a9ff13857558fd350315c35",
                "timestamp": 1660801713767
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "57833dc0-e3f2-43fb-ba20-46480973b0aa",
            "status": 200,
            "result": {
                "orderListId": 1274512,
                "contingencyType": "OCO",
                "listStatusType": "EXEC_STARTED",
                "listOrderStatus": "EXECUTING",
                "listClientOrderId": "08985fedd9ea2cf6b28996",
                "transactionTime": 1660801713793,
                "symbol": "BTCUSDT",
                "orders": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138901,
                        "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138902,
                        "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
                    }
                ],
                "orderReports": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138901,
                        "orderListId": 1274512,
                        "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",
                        "transactTime": 1660801713793,
                        "price": "23410.00000000",
                        "origQty": "0.00650000",
                        "executedQty": "0.00000000",
                        "cummulativeQuoteQty": "0.00000000",
                        "status": "NEW",
                        "timeInForce": "GTC",
                        "type": "STOP_LOSS_LIMIT",
                        "side": "SELL",
                        "stopPrice": "23405.00000000",
                        "workingTime": -1,
                        "selfTradePreventionMode": "NONE"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138902,
                        "orderListId": 1274512,
                        "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",
                        "transactTime": 1660801713793,
                        "price": "23420.00000000",
                        "origQty": "0.00650000",
                        "executedQty": "0.00000000",
                        "cummulativeQuoteQty": "0.00000000",
                        "status": "NEW",
                        "timeInForce": "GTC",
                        "type": "LIMIT_MAKER",
                        "side": "SELL",
                        "workingTime": 1660801713793,
                        "selfTradePreventionMode": "NONE"
                    }
                ]
            },
            "rateLimits": [
                {
                    "rateLimitType": "ORDERS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 50,
                    "count": 2
                },
                {
                    "rateLimitType": "ORDERS",
                    "interval": "DAY",
                    "intervalNum": 1,
                    "limit": 160000,
                    "count": 2
                },
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

    parameters = {
        "symbol": symbol,
        "side": side,
        "price": price,
        "quantity": quantity,
        **kwargs,
    }

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "orderList.place",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def get_oco_order(self, **kwargs):
    """Get OCO order

    Keyword Args:
        orderListId (int): Order list id.
        origClientOrderId (str): Original client order id.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "b53fd5ff-82c7-4a04-bd64-5f9dc42c2100",
            "method": "orderList.status",
            "params": {
                "symbol": "BTCUSDT",
                "origClientOrderId": "08985fedd9ea2cf6b28996"
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "d12f4e8892d46c0ddfbd43d556ff6d818581b3be22a02810c2c20cb719aed6a4",
                "timestamp": 1660801713965
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "b53fd5ff-82c7-4a04-bd64-5f9dc42c2100",
            "status": 200,
            "result": {
            "orderListId": 1274512,
            "contingencyType": "OCO",
            "listStatusType": "EXEC_STARTED",
            "listOrderStatus": "EXECUTING",
            "listClientOrderId": "08985fedd9ea2cf6b28996",
            "transactionTime": 1660801713793,
            "symbol": "BTCUSDT",
            "orders": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569138901,
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569138902,
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
                }
            ]
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

    parameters = {**kwargs}

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "orderList.status",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def cancel_oco_order(self, symbol: str, **kwargs):
    """Cancel OCO order

    Args:
        symbol (str): Symbol to place the order on.
    Keyword Args:
        orderListId (int): Order list id.
        listClientOrderId (str): List client order id.
        newClientOrderId (str): New client order id.
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "c5899911-d3f4-47ae-8835-97da553d27d0",
            "method": "orderList.cancel",
            "params": {
                "symbol": "BTCUSDT",
                "orderListId": 1274512,
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "4973f4b2fee30bf6d45e4a973e941cc60fdd53c8dd5a25edeac96f5733c0ccee",
                "timestamp": 1660801720210
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "c5899911-d3f4-47ae-8835-97da553d27d0",
            "status": 200,
            "result": {
                "orderListId": 1274512,
                "contingencyType": "OCO",
                "listStatusType": "ALL_DONE",
                "listOrderStatus": "ALL_DONE",
                "listClientOrderId": "6023531d7edaad348f5aff",
                "transactionTime": 1660801720215,
                "symbol": "BTCUSDT",
                "orders": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138901,
                        "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138902,
                        "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
                    }
                ],
                "orderReports": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138901,
                        "orderListId": 1274512,
                        "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",
                        "transactTime": 1660801720215,
                        "price": "23410.00000000",
                        "origQty": "0.00650000",
                        "executedQty": "0.00000000",
                        "cummulativeQuoteQty": "0.00000000",
                        "status": "CANCELED",
                        "timeInForce": "GTC",
                        "type": "STOP_LOSS_LIMIT",
                        "side": "SELL",
                        "stopPrice": "23405.00000000",
                        "selfTradePreventionMode": "NONE"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 12569138902,
                        "orderListId": 1274512,
                        "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",
                        "transactTime": 1660801720215,
                        "price": "23420.00000000",
                        "origQty": "0.00650000",
                        "executedQty": "0.00000000",
                        "cummulativeQuoteQty": "0.00000000",
                        "status": "CANCELED",
                        "timeInForce": "GTC",
                        "type": "LIMIT_MAKER",
                        "side": "SELL",
                        "selfTradePreventionMode": "NONE"
                    }
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

    parameters = {"symbol": symbol, **kwargs}

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "orderList.cancel",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)


def get_open_oco_orders(self, **kwargs):
    """Get open OCO orders

    Keyword Args:
        recvWindow (int): Recv window.

    Message sent:

    .. code-block:: json

        {
            "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
            "method": "openOrderLists.status",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "signature": "1bea8b157dd78c3da30359bddcd999e4049749fe50b828e620e12f64e8b433c9",
                "timestamp": 1660801713831
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
            "status": 200,
            "result": [
                {
                    "orderListId": 0,
                    "contingencyType": "OCO",
                    "listStatusType": "EXEC_STARTED",
                    "listOrderStatus": "EXECUTING",
                    "listClientOrderId": "08985fedd9ea2cf6b28996",
                    "transactionTime": 1660801713793,
                    "symbol": "BTCUSDT",
                    "orders": [
                        {
                            "symbol": "BTCUSDT",
                            "orderId": 4,
                            "clientOrderId": "CUhLgTXnX5n2c0gWiLpV4d"
                        },
                        {
                            "symbol": "BTCUSDT",
                            "orderId": 5,
                            "clientOrderId": "1ZqG7bBuYwaF4SU8CwnwHm"
                        }
                    ]
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 1200,
                    "count": 3
                }
            ]
        }

    """

    parameters = {**kwargs}

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "openOrderLists.status",
        "params": websocket_api_signature(self.api_key, self.api_secret, parameters),
    }
    self.send(payload)
