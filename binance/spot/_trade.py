from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def new_order_test(self, symbol: str, side: str, type: str, **kwargs):
    """Test New Order (TRADE)

    Test new order creation and signature/recvWindow. Creates and validates a new order but does not send it into
    the matching engine.

    POST /api/v3/order/test

    https://binance-docs.github.io/apidocs/spot/en/#test-new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
    Keyword Args:
        timeInForce (str, optional)
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/api/v3/order/test"
    return self.sign_request("POST", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """New Order (TRADE)

    Post a new order

    POST /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
    Keyword Args:
        timeInForce (str, optional)
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        strategyId (int, optional)
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/api/v3/order"
    return self.sign_request("POST", url_path, params)


def cancel_order(self, symbol: str, **kwargs):
    """Cancel Order (TRADE)

    Cancel an active order.

    DELETE /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        newClientOrderId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def cancel_open_orders(self, symbol: str, **kwargs):
    """Cancel all Open Orders on a Symbol (TRADE)

    Cancels all active orders on a symbol.
    This includes OCO orders.

    DELETE api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def get_order(self, symbol, **kwargs):
    """Query Order (USER_DATA)

    Check an order's status.

    GET /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def cancel_and_replace(
    self, symbol: str, side: str, type: str, cancelReplaceMode: str, **kwargs
):
    """Cancel an Existing Order and Send a New Order (USER_DATA)

    Cancels an existing order and places a new order on the same symbol.

    Filters are evaluated before the cancel order is placed.

    If the new order placement is successfully sent to the engine, the order count will increase by 1.

    Weight(IP): 1

    POST /api/v3/order/cancelReplace

    https://binance-docs.github.io/apidocs/spot/en/#cancel-an-existing-order-and-send-a-new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
        cancelReplaceMode (str)
    Keyword Args:
        timeInForce (str, optional): Order time in force
        quantity (float, optional): Order quantity
        quoteOrderQty (float, optional): Quote quantity
        price (float, optional): Order price
        cancelNewClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default
        cancelOrigClientOrderId (str, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.
        cancelOrderId (int, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.
        newClientOrderId (str, optional): Used to identify the new order. Automatically generated by default
        strategyId (int, optional)
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        trailingDelta (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [type, "type"],
            [cancelReplaceMode, "cancelReplaceMode"],
        ]
    )

    params = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "cancelReplaceMode": cancelReplaceMode,
        **kwargs,
    }
    url_path = "/api/v3/order/cancelReplace"
    return self.sign_request("POST", url_path, params)


def get_open_orders(self, symbol=None, **kwargs):
    """Current Open Orders (USER_DATA)

    Get all open orders on a symbol.

    GET /api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

    Args:
        symbol (str, optional)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def get_orders(self, symbol: str, **kwargs):
    """All Orders (USER_DATA)

    Get all account orders; active, canceled, or filled.

    GET /api/v3/allOrders

    https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/allOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def new_oco_order(
    self,
    symbol: str,
    side: str,
    quantity: float,
    aboveType: str,
    belowType: str,
    **kwargs
):
    """New Order List - OCO (TRADE)

    Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

    - An OCO has 2 legs called the above leg and below leg.
    - One of the legs must be a LIMIT_MAKER order and the other leg must be STOP_LOSS or STOP_LOSS_LIMIT order.
    - Price restrictions:
        - If the OCO is on the SELL side: LIMIT_MAKER price > Last Traded Price > stopPrice
        - If the OCO is on the BUY side: LIMIT_MAKER price < Last Traded Price < stopPrice
    - OCO counts as 2 orders against the order rate limit.

    Response format for orderReports is selected using the newOrderRespType parameter. The response example is for the RESULT response type. See POST /api/v3/order for more examples.

    POST /api/v3/orderList/oco

    https://binance-docs.github.io/apidocs/spot/en/#new-order-list-oco-trade

    Args:
        symbol (str)
        side (str)
        quantity (float)
        aboveType (str)
        belowType (str)
    Keyword Args:
        listClientOrderId (str, optional): Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. listClientOrderId is distinct from the aboveClientOrderId and the belowCLientOrderId
        aboveClientOrderId (str, optional): Supported values : STOP_LOSS_LIMIT, STOP_LOSS, LIMIT_MAKER
        aboveIcebergQty (int, optional): Note that this can only be used if aboveTimeInForce is GTC.
        abovePrice (float, optional)
        aboveStopPrice (float, optional): Can be used if aboveType is STOP_LOSS or STOP_LOSS_LIMIT. Either aboveStopPrice or aboveTrailingDelta or both, must be specified.
        aboveTrailingDelta (int, optional)
        aboveTimeInForce (float, optional): Required if the aboveType is STOP_LOSS_LIMIT.
        aboveStrategyId (int, optional): Arbitrary numeric value identifying the above leg order within an order strategy.
        aboveStrategyType (int, optional): Arbitrary numeric value identifying the above leg order strategy. Values smaller than 1000000 are reserved and cannot be used.
        belowClientOrderId (str, optional): Arbitrary unique ID among open orders for the below leg order. Automatically generated if not sent
        belowIcebergQty (int, optional): Note that this can only be used if belowTimeInForce is GTC.
        belowPrice (float, optional)
        belowStopPrice (float, optional): Can be used if belowType is STOP_LOSS or STOP_LOSS_LIMIT. Either belowStopPrice or belowTrailingDelta or both, must be specified.
        belowTrailingDelta (int, optional)
        belowTimeInForce (str, optional): Required if the belowType is STOP_LOSS_LIMIT.
        belowStrategyId (int, optional): Arbitrary numeric value identifying the below leg order within an order strategy.
        belowStrategyType (int, optional): Arbitrary numeric value identifying the below leg order strategy. Values smaller than 1000000 are reserved and cannot be used.
        newOrderRespType (str, optional): Select response format: ACK, RESULT, FULL
        selfTradePreventionMode (str, optional): The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [quantity, "quantity"],
            [aboveType, "aboveType"],
            [belowType, "belowType"],
        ]
    )
    params = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "aboveType": aboveType,
        "belowType": belowType,
        **kwargs,
    }

    url_path = "/api/v3/orderList/oco"
    return self.sign_request("POST", url_path, params)


def new_oto_order(
    self,
    symbol: str,
    workingType: str,
    workingSide: str,
    workingPrice: float,
    workingQuantity: float,
    pendingType: str,
    pendingSide: str,
    pendingQuantity: float,
    **kwargs
):
    """New Order List - OTO (TRADE)


    - An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
    - The first order is called the working order and must be LIMIT or LIMIT_MAKER. Initially, only the working order goes on the order book.
    - The second order is called the pending order. It can be any order type except for MARKET orders using parameter quoteOrderQty. The pending order is only placed on the order book when the working order gets fully filled.
    - If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
    - When the order list is placed, if the working order gets immediately fully filled, the placement response will show the working order as FILLED but the pending order will still appear as PENDING_NEW. You need to query the status of the pending order again to see its updated status.
    - OTOs count as 2 orders against the order rate limit, EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.

    POST /api/v3/orderList/oto

    https://binance-docs.github.io/apidocs/spot/en/#new-order-list-oto-trade

    Args:
        symbol (str)
        workingType (str)
        workingSide (str)
        workingPrice (float)
        workingQuantity (float)
        pendingType (str)
        pendingSide (str)
        pendingQuantity (float)
    Keyword Args:
        listClientOrderId (str, optional): Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. listClientOrderId is distinct from the workingClientOrderId and the pendingClientOrderId
        newOrderRespType (str, optional): Format of the JSON response. Supported values: ACK, FULL, RESULT
        selfTradePreventionMode (str, optional): The allowed values are dependent on what is configured on the symbol.
        workingClientOrderId (str, optional): Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
        workingIcebergQty (float, optional): This can only be used if workingTimeInForce is GTC or if workingType is LIMIT_MAKER.
        workingTimeInForce (str, optional): Supported values: FOK, IOC, GTC
        workingStrategyId (int, optional): Arbitrary numeric value identifying the working order within an order strategy.
        workingStrategyType (int, optional): Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.
        pendingClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.
        pendingPrice (float, optional)
        pendingStopPrice (float, optional)
        pendingTrailingDelta (float, optional)
        pendingIcebergQty (float, optional): This can only be used if pendingTimeInForce is GTC or if pendingType is LIMIT_MAKER.
        pendingTimeInForce (str, optional): Supported values: GTC, FOK, IOC
        pendingStrategyId (int, optional): Arbitrary numeric value identifying the pending order within an order strategy.
        pendingStrategyType (int, optional): Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [workingType, "workingType"],
            [workingSide, "workingSide"],
            [workingPrice, "workingPrice"],
            [workingQuantity, "workingQuantity"],
            [pendingType, "pendingType"],
            [pendingSide, "pendingSide"],
            [pendingQuantity, "pendingQuantity"],
        ]
    )
    params = {
        "symbol": symbol,
        "workingType": workingType,
        "workingSide": workingSide,
        "workingPrice": workingPrice,
        "workingQuantity": workingQuantity,
        "pendingType": pendingType,
        "pendingSide": pendingSide,
        "pendingQuantity": pendingQuantity,
        **kwargs,
    }

    url_path = "/api/v3/orderList/oto"
    return self.sign_request("POST", url_path, params)


def new_otoco_order(
    self,
    symbol: str,
    workingType: str,
    workingSide: str,
    workingPrice: float,
    workingQuantity: float,
    pendingSide: str,
    pendingQuantity: float,
    pendingAboveType: str,
    **kwargs
):
    """New Order List - OTOCO (TRADE)

    Place an OTOCO.

    - An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
    - The first order is called the working order and must be LIMIT or LIMIT_MAKER. Initially, only the working order goes on the order book.
        - The behavior of the working order is the same as the OTO.
    - OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets fully filled.
        - The rules of the pending above and pending below follow the same rules as the Order List OCO.
    - OTOCOs count as 3 orders against the order rate limit, EXCHANGE_MAX_NUM_ORDERS filter, and MAX_NUM_ORDERS filter.

    POST /api/v3/orderList/otoco

    https://binance-docs.github.io/apidocs/spot/en/#new-order-list-oto-trade

    Args:
        symbol (str)
        workingType (str)
        workingSide (str)
        workingPrice (float)
        workingQuantity (float)
        pendingSide (str)
        pendingQuantity (float)
        pendingAboveType (str)
    Keyword Args:
        listClientOrderId (str, optional): Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. listClientOrderId is distinct from the workingClientOrderId, pendingAboveClientOrderId, and the pendingBelowClientOrderId.
        newOrderRespType (str, optional): Format the JSON response. Supported values: ACK, FULL, RESPONSE
        selfTradePreventionMode (str, optional): The allowed values are dependent on what is configured on the symbol.
        workingClientOrderId (str, optional): Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
        workingIcebergQty (float, optional): This can only be used if workingTimeInForce is GTC or if workingType is LIMIT_MAKER.
        workingTimeInForce (str, optional): Supported values: GTC, IOC, FOK
        workingStrategyId (int, optional): Arbitrary numeric value identifying the working order within an order strategy.
        workingStrategyType (int, optional): Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.
        pendingAboveClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.
        pendingAbovePrice (float, optional)
        pendingAboveStopPrice (float, optional)
        pendingAboveTrailingDelta (float, optional)
        pendingAboveIcebergQty (float, optional): This can only be used if pendingAboveTimeInForce is GTC or if pendingAboveType is LIMIT_MAKER.
        pendingAboveTimeInForce (str, optional)
        pendingAboveStrategyId (int, optional): Arbitrary numeric value identifying the pending above order within an order strategy.
        pendingAboveStrategyType (int, optional): Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used.
        pendingBelowType (str, optional): Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
        pendingBelowClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.
        pendingBelowPrice (float, optional)
        pendingBelowStopPrice (float, optional)
        pendingBelowTrailingDelta (float, optional)
        pendingBelowIcebergQty (float, optional): This can only be used if pendingBelowTimeInForce is GTC or if pendingBelowType is LIMIT_MAKER.
        pendingBelowTimeInForce (str, optional)
        pendingBelowStrategyId (int, optional): Arbitrary numeric value identifying the pending below order within an order strategy.
        pendingBelowStrategyType (int, optional): Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [workingType, "workingType"],
            [workingSide, "workingSide"],
            [workingPrice, "workingPrice"],
            [workingQuantity, "workingQuantity"],
            [pendingSide, "pendingSide"],
            [pendingQuantity, "pendingQuantity"],
            [pendingAboveType, "pendingAboveType"],
        ]
    )
    params = {
        "symbol": symbol,
        "workingType": workingType,
        "workingSide": workingSide,
        "workingPrice": workingPrice,
        "workingQuantity": workingQuantity,
        "pendingSide": pendingSide,
        "pendingQuantity": pendingQuantity,
        "pendingAboveType": pendingAboveType,
        **kwargs,
    }

    url_path = "/api/v3/orderList/otoco"
    return self.sign_request("POST", url_path, params)


def cancel_oco_order(self, symbol, **kwargs):
    """Cancel OCO (TRADE)

    Cancel an entire Order List

    DELETE /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#cancel-order-lists-trade

    Args:
        symbol (str)
    Keyword Args:
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        listClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/orderList"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def get_oco_order(self, **kwargs):
    """Query OCO (USER_DATA)

    Retrieves a specific OCO based on provided optional parameters

    GET /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#query-order-lists-user_data

    Keyword Args:
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        origClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/api/v3/orderList"
    return self.sign_request("GET", url_path, {**kwargs})


def get_oco_orders(self, **kwargs):
    """Query all OCO (USER_DATA)

    Retrieves all OCO based on provided optional parameters

    GET /api/v3/allOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-all-order-lists-user_data

    Keyword Args:
        fromId (int, optional): If supplied, neither startTime or endTime can be provided
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/allOrderList"
    return self.sign_request("GET", url_path, {**kwargs})


def get_oco_open_orders(self, **kwargs):
    """Query Open OCO (USER_DATA)

    GET /api/v3/openOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-open-order-lists-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/openOrderList"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """Account Information (USER_DATA)

    Get current account information

    GET /api/v3/account

    https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/account"
    return self.sign_request("GET", url_path, {**kwargs})


def my_trades(self, symbol: str, **kwargs):
    """Account Trade List (USER_DATA)

    Get trades for a specific account and symbol.

    GET /api/v3/myTrades

    https://binance-docs.github.io/apidocs/spot/en/#account-trade-list-user_data

    Args:
        symbol (str)
    Keyword Args:
        fromId (int, optional): TradeId to fetch from. Default gets most recent trades.
        orderId (int, optional): This can only be used in combination with symbol
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/myTrades"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def get_order_rate_limit(self, **kwargs):
    """Query Current Order Count Usage (TRADE)

    Displays the user's current order count usage for all intervals.

    GET /api/v3/rateLimit/order

    https://binance-docs.github.io/apidocs/spot/en/#query-current-order-count-usage-trade

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/rateLimit/order"
    return self.sign_request("GET", url_path, {**kwargs})


def query_prevented_matches(self, symbol: str, **kwargs):
    """Query Prevented Matches (USER_DATA)

    Displays the list of orders that were expired because of STP.

    For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to our STP FAQ page.

    These are the combinations supported:

    * symbol + preventedMatchId
    * symbol + orderId
    * symbol + orderId + fromPreventedMatchId (limit will default to 500)
    * symbol + orderId + fromPreventedMatchId + limit

    Weight(IP):

    Case 	                          Weight
    If symbol is invalid: 	        2
    Querying by preventedMatchId: 	2
    Querying by orderId: 	          20

    GET /api/v3/myPreventedMatches

    https://binance-docs.github.io/apidocs/spot/en/#query-prevented-matches-user_data

    Args:
        symbol (str)
    Keyword Args:
        preventedMatchId (int, optional)
        orderId (int, optional): Order id
        fromPreventedMatchId (int, optional)
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/myPreventedMatches"
    return self.sign_request("GET", url_path, params)


def query_allocations(self, symbol: str, **kwargs):
    """Query Cross-Collateral Information (USER_DATA)

    GET /api/v3/myAllocations

    https://binance-docs.github.io/apidocs/spot/en/#query-allocations-user_data

    Args:
        symbol (str)
    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        fromAllocationId (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        orderId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/myAllocations"
    return self.sign_request("GET", url_path, params)


def query_commission_rates(self, symbol: str, **kwargs):
    """Query Commission Rates (USER_DATA)

    GET /api/v3/account/commission

    https://binance-docs.github.io/apidocs/spot/en/#query-commission-rates-user_data

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/account/commission"
    return self.sign_request("GET", url_path, params)
