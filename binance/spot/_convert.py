from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def list_all_convert_pairs(self, **kwargs):
    """List All Convert Pairs

    Query for all convertible token pairs and the tokens’ respective upper/lower limits

    Weight(IP): 3000

    GET /sapi/v1/convert/exchangeInfo

    https://binance-docs.github.io/apidocs/spot/en/#list-all-convert-pairs

    Keyword Args:
        fromAsset (str, optional): User spends coin
        toAsset (str, optional): User receives coin
    """

    url_path = "/sapi/v1/convert/exchangeInfo"
    return self.query(url_path, {**kwargs})


def query_order_quantity_precision_per_asset(self, **kwargs):
    """Query order quantity precision per asset (USER_DATA)

    Query for supported asset precision information

    Weight(IP): 100

    GET /sapi/v1/convert/assetInfo

    https://binance-docs.github.io/apidocs/spot/en/#query-order-quantity-precision-per-asset-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/convert/assetInfo"
    return self.sign_request("GET", url_path, {**kwargs})


def send_quote_request(self, fromAsset: str, toAsset: str, **kwargs):
    """Send quote request (USER_DATA)

    Request a quote for the requested token pairs

    Weight(UID): 200

    POST /sapi/v1/convert/getQuote

    https://binance-docs.github.io/apidocs/spot/en/#send-quote-request-user_data

    Args:
        fromAsset (str)
        toAsset (str)
    Keyword Args:
        fromAmount (float, optional): When specified, it is the amount you will be debited after the conversion
        toAmount (float, optional): When specified, it is the amount you will be debited after the conversion
        validTime (str, optional): 10s, 30s, 1m, 2m, default 10s
        walletType (str, optional): SPOT or FUNDING. Default is SPOT
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[fromAsset, "fromAsset"], [toAsset, "toAsset"]])

    params = {"fromAsset": fromAsset, "toAsset": toAsset, **kwargs}
    url_path = "/sapi/v1/convert/getQuote"
    return self.sign_request("POST", url_path, params)


def accept_quote(self, quoteId: str, **kwargs):
    """Accept Quote (TRADE)

    Accept the offered quote by quote ID.

    Weight(UID): 500

    POST /sapi/v1/convert/acceptQuote

    https://binance-docs.github.io/apidocs/spot/en/#accept-quote-trade

    Args:
        quoteId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(quoteId, "quoteId")

    params = {"quoteId": quoteId, **kwargs}
    url_path = "/sapi/v1/convert/acceptQuote"
    return self.sign_request("POST", url_path, params)


def order_status(self, **kwargs):
    """Order status (USER_DATA)

    Query order status by order ID.

    Weight(UID): 100

    GET /sapi/v1/convert/orderStatus

    https://binance-docs.github.io/apidocs/spot/en/#order-status-user_data

    Keyword Args:
        orderId (str, optional)
        quoteId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/convert/orderStatus"
    return self.sign_request("GET", url_path, {**kwargs})


def place_limit_order(
    self,
    baseAsset: str,
    quoteAsset: str,
    limitPrice: float,
    side: str,
    expiredType: str,
    **kwargs
):
    """Place limit order (USER_DATA)

    POST /sapi/v1/convert/limit/placeOrder

    https://binance-docs.github.io/apidocs/spot/en/#place-limit-order-user_data

    Args:
        baseAsset (str): base asset (use the response fromIsBase from GET /sapi/v1/convert/exchangeInfo api to check which one is baseAsset)
        quoteAsset (str): quote asset
        limitPrice (float): Symbol limit price (from baseAsset to quoteAsset)
        side (str): BUY or SELL
        expiredType (str): 1_D, 3_D, 7_D, 30_D (D means day)
    Keyword Args:
        baseAmount (float, optional): Base asset amount. (One of baseAmount or quoteAmount is required)
        quotrAmount (float, optional): Quote asset amount. (One of baseAmount or quoteAmount is required)
        walletType (str, optional): SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [baseAsset, "baseAsset"],
            [quoteAsset, "quoteAsset"],
            [limitPrice, "limitPrice"],
            [side, "side"],
            [expiredType, "expiredType"],
        ]
    )

    params = {
        "baseAsset": baseAsset,
        "quoteAsset": quoteAsset,
        "limitPrice": limitPrice,
        "side": side,
        "expiredType": expiredType,
        **kwargs,
    }
    url_path = "/sapi/v1/convert/limit/placeOrder"
    return self.sign_request("POST", url_path, params)


def cancel_limit_order(self, orderId: str, **kwargs):
    """Cancel limit order (USER_DATA)

    POST /sapi/v1/convert/limit/cancelOrder

    https://binance-docs.github.io/apidocs/spot/en/#cancel-limit-order-user_data

    Args:
        orderId (str): The orderId from placeOrder api
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(orderId, "orderId")

    params = {"orderId": orderId, **kwargs}
    url_path = "/sapi/v1/convert/limit/cancelOrder"
    return self.sign_request("POST", url_path, params)


def query_limit_open_order(self, **kwargs):
    """Query limit open orders (USER_DATA)

    GET /sapi/v1/convert/limit/queryOpenOrders

    https://binance-docs.github.io/apidocs/spot/en/#query-limit-open-orders-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/convert/limit/queryOpenOrders"
    return self.sign_request("GET", url_path, {**kwargs})


def get_convert_trade_history(self, startTime: int, endTime: int, **kwargs):
    """Get Convert Trade History (USER_DATA)

    - The max interval between startTime and endTime is 30 days.

    Weight(UID): 3000

    GET /sapi/v1/convert/tradeFlow

    https://binance-docs.github.io/apidocs/spot/en/#get-convert-trade-history-user_data

    Args:
        startTime (int)
        endTime (int)
    Keyword Args:
        limit (int, optional): default 100, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

    params = {"startTime": startTime, "endTime": endTime, **kwargs}
    url_path = "/sapi/v1/convert/tradeFlow"
    return self.sign_request("GET", url_path, params)
