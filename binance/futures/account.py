import json

from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def change_position_side(self, dual_side_position: str, **kwargs):
    """Change Position Mode(TRADE)

    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

    POST /fapi/v1/positionSide/dual

    https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

    Args:
        dual_side_position (str) "true": Hedge Mode; "false": One-way Mode
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameters([[dual_side_position, "dualSidePosition"]])
    params = {"dualSidePosition": dual_side_position, **kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("POST", url_path, params)


def position_side(self, **kwargs):
    """Get Current Position Mode(USER_DATA)

    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

    GET /fapi/v1/positionSide/dual (HMAC SHA256)

    https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

    Keyword Args:
        recvWindow (int, optional)
    """
    params = {**kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("GET", url_path, params)


def change_multi_assets_margin(self, multi_assets_margin: str, **kwargs):
    """Change Multi-Assets Mode (TRADE)

    Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

    POST /fapi/v1/multiAssetsMargin (HMAC SHA256)

    https://binance-docs.github.io/apidocs/futures/en/#change-multi-assets-mode-trade

    Args:
        multi_assets_margin (str) "true": Multi-Assets Mode; "false": Single-Asset Mode
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameter(multi_assets_margin, "multiAssetsMargin")
    params = {"multiAssetsMargin": multi_assets_margin, **kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("POST", url_path, params)


def get_multi_assets_margin(self, **kwargs):
    """Get Current Multi-Assets Mode (USER_DATA)

    Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

    GET /fapi/v1/multiAssetsMargin (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data

    Keyword Args:
        recvWindow (int, optional)
    """
    params = {**kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("GET", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """New Order (TRADE)

    Send in a new order.

    POST /fapi/v1/order (HMAC SHA256)

    https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

    Args:
        symbol (str): the trading pair
        side (str): the trading side eg. BUY
        type (str): eg. TRAILING_STOP_MARKET
    Keyword Args:
        positionSide (str, optional) : Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in
                                       Hedge Mode.
        timeInForce (str, optional):
        quantity (float, optional): Cannot be sent with closePosition=true(Close-All)
        reduceOnly (str, optional): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with
                                    closePosition=true
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent. Can only be
                                         string following the rule: ^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice (float, optional): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        closePosition (str, optional): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        activationPrice (float, optional): Used with TRAILING_STOP_MARKET orders, default as the latest price(supporting
                                          different workingType)
        callbackRate (float, optional): Used with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%
        workingType (str, optional): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        priceProtect (str, optional): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        newOrderRespType (str, optional): "ACK", "RESULT", default "ACK"
        recvWindow (int, optional)
    Additional Mandatory parameters based on type:
        LIMIT: timeInForce, quantity, price
        MARKET: quantity
        STOP/TAKE_PROFIT: quantity, price, stopPrice
        STOP_MARKET/TAKE_PROFIT_MARKET: stopPrice
        TRAILING_STOP_MARKET: callbackRate
    """
    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order"
    return self.sign_request("POST", url_path, params)


def new_batch_orders(self, batch_orders: list, **kwargs):
    """Place Multiple Orders (TRADE)

    Send multiple orders.

    POST /fapi/v1/batchOrders (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

    Args:
        batch_orders (list): order list. Max 5 orders
    Where batchOrders is the list of order parameters in JSON:
        symbol (str)
        side (str)
        positionSide (str, optional): Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode.
                                       It must be sent with Hedge Mode.

        type (str)
        timeInForce (str, optional)
        quantity (float)
        reduceOnly (str, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent. Can only
                                            be string following the rule: ^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice (float, optional): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        activationPrice (float, optional): Used with TRAILING_STOP_MARKET orders, default as the latest price(supporting
                                           different workingType)
        callbackRate (float, optional): Used with TRAILING_STOP_MARKET orders, min 0.1, max 4 where 1 for 1%
        workingType (str, optional): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"
        priceProtect (str, optional): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/
                                       TAKE_PROFIT_MARKET orders.
        newOrderRespType (str, optional): "ACK", "RESULT", default "ACK"

        Notes:
            Parameter rules are same with New Order
            Batch orders are processed concurrently, and the order of matching is not guaranteed.
            The order of returned contents for batch orders is the same as the order of the order list.
    """
    check_required_parameter(batch_orders, "batchOrders")
    params = {"batchOrders": json.dumps(batch_orders), **kwargs}
    url_path = "/fapi/v1/batchOrders"
    return self.sign_request("POST", url_path, params)


def get_order(self, symbol: str,  **kwargs):
    """Query Order (USER_DATA)

    Check an order's status.

    GET /fapi/v1/order (HMAC SHA256)


    https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        recvWindow (int, optional)

    Either orderId or origClientOrderId must be sent.
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/fapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def cancel_order(self, symbol: str,  **kwargs):
    """Cancel Order (TRADE)

    Cancel an active order.

    DELETE /fapi/v1/order (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#cancel-order-trade

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        recvWindow (int, optional)

    Either orderId or origClientOrderId must be sent.
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/fapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def cancel_all_orders(self, symbol: str,  **kwargs):
    """Cancel All Open Orders (TRADE)

    Cancel all orders.

    DELETE /fapi/v1/allOpenOrders (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#cancel-all-open-orders-trade

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional)

    """
    check_required_parameter(symbol, "symbol")

    url_path = "/fapi/v1/allOpenOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def cancel_batch_orders(self, symbol: str,  **kwargs):
    """Cancel Multiple Orders (TRADE)

    Cancel multiple orders.

    DELETE /fapi/v1/batchOrders (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#cancel-multiple-orders-trade

    Args:
        symbol (str)
    Keyword Args:
        orderIdList (list, optional): max length 10 e.g. [1234567,2345678]
        origClientOrderIdList (list, optional): max length 10 e.g. ["my_id_1","my_id_2"], encode the double quotes.
                                               No space after comma.
        recvWindow (int, optional)

    Either orderIdList or origClientOrderIdList must be sent.
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/fapi/v1/batchOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def auto_cancel_all(self, symbol: str, count_down_time: int,  **kwargs):
    """Auto-Cancel All Open Orders (TRADE)

    Cancel all open orders of the specified symbol at the end of the specified countdown.


    POST /fapi/v1/countdownCancelAll (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#auto-cancel-all-open-orders-trade

    Args:
        symbol (str)
        count_down_time (int) countdown time, 1000 for 1 second. 0 to cancel the timer
    Keyword Args:
        recvWindow (int, optional)

    The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and
    replaced by a new one.

    Example usage:
        Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
        If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically
        canceled.
        If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.

    The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy
        should be considered when using this function. We do not recommend setting the countdown time to be too precise
        or too small.
    """
    check_required_parameters([[symbol, "symbol"], [count_down_time, "countdownTime"]])
    url_path = "/fapi/v1/countdownCancelAll"
    payload = {"symbol": symbol, "countdownTime": count_down_time, **kwargs}
    return self.sign_request("POST", url_path, payload)


def get_open_order(self, symbol: str,  **kwargs):
    """Query Current Open Order (USER_DATA)

    GET /fapi/v1/openOrder (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#query-current-open-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (int, optional)
        recvWindow (int, optional)

    Either orderId or origClientOrderId must be sent
    If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/fapi/v1/openOrder"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def get_open_orders(self, **kwargs):
    """Current All Open Orders (USER_DATA)

    Get all open orders on a symbol. Careful when accessing this with no symbol.

    GET /fapi/v1/openOrders (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#current-all-open-orders-user_data

    Keyword Args:
        symbol (str, optional)  If the symbol is not sent, orders for all symbols will be returned in an array.
        recvWindow (int, optional)
    """
    url_path = "/fapi/v1/openOrders"
    payload = {**kwargs}
    return self.sign_request("GET", url_path, payload)


def get_all_orders(self, symbol: str, **kwargs):
    """All Orders (USER_DATA)

    Get all account orders; active, canceled, or filled.

    These orders will not be found:
        order status is CANCELED or EXPIRED, AND
        order has NO filled trade, AND
        created time + 7 days < current time

    GET /fapi/v1/allOrders (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#all-orders-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit Default 500; max 1000.
        recvWindow (int, optional)

    Notes:
        If orderId is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        The query time period must be less then 7 days( default as the recent 7 days)
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/allOrders"
    return self.sign_request("GET", url_path, payload)


def balance(self, **kwargs):
    """Futures Account Balance V2 (USER_DATA)

    GET /fapi/v2/balance (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#futures-account-balance-v2-user_data


    Keyword Args:
        recvWindow (int, optional)
    """
    payload = {**kwargs}
    url_path = "/fapi/v2/balance"
    return self.sign_request("GET", url_path, payload)


def account(self, **kwargs):
    """Account Information V2 (USER_DATA)

    Get current account information.

    GET /fapi/v2/account (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#account-information-v2-user_data


    Keyword Args:
        recvWindow (int, optional)
    """
    payload = {**kwargs}
    url_path = "/fapi/v2/account"
    return self.sign_request("GET", url_path, payload)


def change_leverage(self, symbol: str, leverage: int, **kwargs):
    """Change Initial Leverage (TRADE)

    Change user's initial leverage of specific symbol market.

    POST /fapi/v1/leverage (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#change-initial-leverage-trade

    Args:
        symbol (str)
        leverage (int) target initial leverage: int from 1 to 125
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameters([[symbol, "symbol"], [leverage, "leverage"]])
    payload = {"symbol": symbol, "leverage": leverage, **kwargs}
    url_path = "/fapi/v1/leverage"
    return self.sign_request("POST", url_path, payload)


def change_margin(self, symbol: str, margin_type: int, **kwargs):
    """Change Margin Type (TRADE)

    POST /fapi/v1/marginType (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#change-margin-type-trade

    Args:
        symbol (str)
        margin_type (str) ISOLATED, CROSSED
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameters([[symbol, "symbol"], [margin_type, "marginType"]])
    payload = {"symbol": symbol, "marginType": margin_type, **kwargs}
    url_path = "/fapi/v1/marginType"
    return self.sign_request("POST", url_path, payload)


def change_position_margin(self, symbol: str, amount: float, type: int, **kwargs):
    """Modify Isolated Position Margin (TRADE)
       Only for isolated symbol

    POST /fapi/v1/positionMargin (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#modify-isolated-position-margin-trade

    Args:
        symbol (str)
        amount (float)
        type (int) 1: Add position margin，2: Reduce position margin
    Keyword Args:
        position_side (str, optional) Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
        recvWindow (int, optional)
    """
    check_required_parameters([[symbol, "symbol"], [amount, "amount"], [type, "type"]])
    payload = {"symbol": symbol, "amount": amount, "type": type, **kwargs}
    url_path = "/fapi/v1/positionMargin"
    return self.sign_request("POST", url_path, payload)


def margin_position_history(self, symbol: str, **kwargs):
    """Get Position Margin Change History (TRADE)

    GET /fapi/v1/positionMargin/history (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#get-position-margin-change-history-trade

    Args:
        symbol (str)
    Keyword Args:
        type (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default: 500
        recvWindow (int, optional)
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/positionMargin/history"
    return self.sign_request("GET", url_path, payload)


def risk(self, **kwargs):
    """Position Information V2 (USER_DATA)
    Get current position information.

    GET /fapi/v2/positionRisk (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#position-information-v2-user_data


    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional)
    Note:
        Please use with user data stream ACCOUNT_UPDATE to meet your timeliness and accuracy needs.
    """
    payload = {**kwargs}
    url_path = "/fapi/v2/positionRisk"
    return self.sign_request("GET", url_path, payload)


def trades(self, symbol: str, **kwargs):
    """Account Trade List (USER_DATA)

    Get trades for a specific account and symbol.


    GET /fapi/v1/userTrades (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#account-trade-list-user_data


    Args:
        symbol (str)
    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        fromId (int, optional) Trade id to fetch from. Default gets most recent trades.
        limit (int, optional) Default 500; max 1000.
        recvWindow (int, optional)
    Notes:
        If startTime and endTime are both not sent, then the last 7 days' data will be returned.
        The time between startTime and endTime cannot be longer than 7 days.
        The parameter fromId cannot be sent with startTime or endTime.
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/userTrades"
    return self.sign_request("GET", url_path, payload)


def income(self, **kwargs):
    """Get Income History(USER_DATA)

    GET /fapi/v1/income (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data

    Keyword Args:
        symbol (str, optional)
        incomeType (str, optional): "TRANSFER"，"WELCOME_BONUS", "REALIZED_PNL"，"FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR"
        startTime (int, optional): Timestamp in ms to get funding from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get funding until INCLUSIVE.
        limit (int, optional) Default 500; max 1000.
        recvWindow (int, optional)
    Notes:
        If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        If incomeType is not sent, all kinds of flow will be returned
        "tranId" is unique in the same incomeType for a user
    """
    payload = {**kwargs}
    url_path = "/fapi/v1/income"
    return self.sign_request("GET", url_path, payload)


def brackets(self, **kwargs):
    """Notional and Leverage Brackets (USER_DATA)

    GET /fapi/v1/leverageBracket


    https://binance-docs.github.io/apidocs/futures/en/#notional-and-leverage-brackets-user_data

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional)
    """
    payload = {**kwargs}
    url_path = "/fapi/v1/leverageBracket"
    return self.sign_request("GET", url_path, payload)


def adl_quantile(self, **kwargs):
    """Position ADL Quantile Estimation (USER_DATA)

    GET /fapi/v1/adlQuantile


    https://binance-docs.github.io/apidocs/futures/en/#position-adl-quantile-estimation-user_data

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional)
    Notes:
        Values update every 30s.
        Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
        For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
        If the positions of the symbol are crossed margined in Hedge Mode:
        "HEDGE" as a sign will be returned instead of "BOTH";
        A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
    """
    payload = {**kwargs}
    url_path = "/fapi/v1/adlQuantile"
    return self.sign_request("GET", url_path, payload)


def force_orders(self, **kwargs):
    """User's Force Orders (USER_DATA)

    GET /fapi/v1/forceOrders


    https://binance-docs.github.io/apidocs/futures/en/#user-39-s-force-orders-user_data

    Keyword Args:
        symbol (str, optional)
        autoCloseType (str, optional): "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 50; max 100.
        recvWindow (int, optional)
    Notes:
        If "autoCloseType" is not sent, orders with both of the types will be returned
        If "startTime" is not sent, data within 7 days before "endTime" can be queried
    """
    payload = {**kwargs}
    url_path = "/fapi/v1/forceOrders"
    return self.sign_request("GET", url_path, payload)


def status(self, **kwargs):
    """User API Trading Quantitative Rules Indicators (USER_DATA)

    GET /fapi/v1/apiTradingStatus


    https://binance-docs.github.io/apidocs/futures/en/#user-api-trading-quantitative-rules-indicators-user_data

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional)
    """
    payload = {**kwargs}
    url_path = "/fapi/v1/apiTradingStatus"
    return self.sign_request("GET", url_path, payload)


def commission(self, symbol: str, **kwargs):
    """User Commission Rate (USER_DATA)

    GET /fapi/v1/commissionRate (HMAC SHA256)


    https://binance-docs.github.io/apidocs/futures/en/#user-commission-rate-user_data

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional)
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/commissionRate"
    return self.sign_request("GET", url_path, payload)


