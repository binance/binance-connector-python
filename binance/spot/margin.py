from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def margin_transfer(self, asset: str, amount, type: int, **kwargs):
    """Margin Account Transfer (MARGIN)
    Execute transfer between spot account and margin account.

    POST /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-transfer-margin

    Args:
        asset (str): The asset being transferred, e.g., BTC.
        amount (float): The amount to be transferred
        type (int): 1: transfer from main account to cross margin account
                    2: transfer from cross margin account to main account
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [amount, "amount"], [type, "type"]])

    payload = {"asset": asset, "amount": amount, "type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/transfer", payload)


def margin_borrow(self, asset: str, amount, **kwargs):
    """Margin Account Borrow (MARGIN)
    Apply for a loan.

    POST /sapi/v1/margin/load

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-borrow-margin

    Args:
        asset (str): The asset being transferred, e.g., BTC.
        amount (float): The amount to be transferred
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        symbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [amount, "amount"]])

    payload = {"asset": asset, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/loan", payload)


def margin_repay(self, asset: str, amount, **kwargs):
    """Margin Account Repay(MARGIN)
    Repay loan for margin account.

    POST /sapi/v1/margin/repay

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-repay-margin

    Args:
        asset (str): The asset being transferred, e.g., BTC.
        amount (float): The amount to be transferred
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        symbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [amount, "amount"]])

    payload = {"asset": asset, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/repay", payload)


def margin_asset(self, asset: str):
    """Query Margin Asset (MARKET_DATA)

    GET /sapi/v1/margin/asset

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-asset-market_data

    Args:
        asset (str): The asset being transferred, e.g., BTC.

    """

    check_required_parameter(asset, "asset")

    payload = {"asset": asset}
    return self.limit_request("GET", "/sapi/v1/margin/asset", payload)


def margin_pair(self, symbol: str):
    """Query Margin Pair (MARKET_DATA)

    GET /sapi/v1/margin/pair

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-pair-market_data

    Args:
        symbol (str)
    """

    check_required_parameter(symbol, "symbol")

    payload = {"symbol": symbol}
    return self.limit_request("GET", "/sapi/v1/margin/pair", payload)


def margin_all_assets(self):
    """Get All Margin Assets (MARKET_DATA)

    GET /sapi/v1/margin/allAssets

    https://binance-docs.github.io/apidocs/spot/en/#get-all-margin-assets-market_data

    """

    return self.limit_request("GET", "/sapi/v1/margin/allAssets")


def margin_all_pairs(self):
    """Get All Margin Pairs (MARKET_DATA)

    GET /sapi/v1/margin/allPairs

    https://binance-docs.github.io/apidocs/spot/en/#get-all-margin-pairs-market_data

    """

    return self.limit_request("GET", "/sapi/v1/margin/allPairs")


def margin_pair_index(self, symbol: str, **kwargs):
    """Query Margin PriceIndex (MARKET_DATA)

    GET /sapi/v1/margin/priceIndex

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-priceindex-market_data

    Args:
        symbol (str)
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/sapi/v1/margin/priceIndex", payload)


def new_margin_order(self, symbol: str, side: str, type: str, **kwargs):
    """Margin Account New Order (TRADE)

    Post a new order for margin account.

    POST /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-new-order-trade

    Args:
        symbol (str)
        side (str): BUY or SELL
        type (str)
    Keyword Args:
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        stopPrice (float, optional): Used with STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT and TAKE_PROFIT_LIMIT orders.
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        sideEffectType (str, optional): NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.
        timeInForce (str, optional): GTC,IOC,FOK
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [type, "type"],
        ]
    )

    payload = {"symbol": symbol, "side": side, "type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/order", payload)


def cancel_margin_order(self, symbol: str, **kwargs):
    """Margin Account Cancel Order (TRADE)

     Cancel an active order for margin account.

    DELETE /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-order-trade

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", "/sapi/v1/margin/order", payload)


def margin_transfer_history(self, asset: str, **kwargs):
    """Get Transfer History (USER_DATA)

    GET /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-transfer-history-user_data

    Args:
        asset (str)
    Keyword Args:
        type (str, optional): Transfer Type: ROLL_IN, ROLL_OUT
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/transfer", payload)


def margin_load_record(self, asset: str, **kwargs):
    """Query Loan Record (USER_DATA)

    GET /sapi/v1/margin/loan

    https://binance-docs.github.io/apidocs/spot/en/#query-loan-record-user_data

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        txId (int, optional): the tranId in POST /sapi/v1/margin/loan
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/loan", payload)


def margin_repay_record(self, asset: str, **kwargs):
    """Query Repay Record (USER_DATA)

    GET /sapi/v1/margin/repay

    https://binance-docs.github.io/apidocs/spot/en/#query-repay-record-user_data

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        txId (int, optional): return of /sapi/v1/margin/repay
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/repay", payload)


def margin_interest_history(self, **kwargs):
    """Get Interest History (USER_DATA)

    GET /sapi/v1/margin/interestHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data

    Keyword Args:
        asset (str, optional)
        isolatedSymbol (str, optional): isolated symbol
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/interestHistory", kwargs)


def margin_force_liquidation_record(self, **kwargs):
    """Get Force Liquidation Record (USER_DATA)

    GET /sapi/v1/margin/forceLiquidationRec

    https://binance-docs.github.io/apidocs/spot/en/#get-force-liquidation-record-user_data

    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/forceLiquidationRec", kwargs)


def margin_account(self, **kwargs):
    """Query Cross Margin Account Details (USER_DATA)

    GET /sapi/v1/margin/account

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-details-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/account", kwargs)


def margin_order(self, symbol: str, **kwargs):
    """Query Margin Account's Order (USER_DATA)

    GET /sapi/v1/margin/order

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (str, optional)
        origClientOrderId (str, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/order", payload)


def margin_open_orders(self, **kwargs):
    """Query Margin Account's Open Order (USER_DATA)

    GET /sapi/v1/margin/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-open-order-user_data

    Keyword Args:
        symbol (str, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/openOrders", kwargs)


def margin_open_orders_cancellation(self, symbol: str, **kwargs):
    """Margin Account Cancel all Open Orders on a Symbol (USER_DATA)

    DELETE /sapi/v1/margin/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-all-open-orders-on-a-symbol-trade

    Args:
        symbol (str)
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", "/sapi/v1/margin/openOrders", payload)


def margin_all_orders(self, symbol: str, **kwargs):
    """Query Margin Account's All Orders (USER_DATA)

    GET /sapi/v1/margin/allOrders

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-all-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 500.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/allOrders", payload)


def margin_my_trades(self, symbol: str, **kwargs):
    """Query Margin Account's Trade List (USER_DATA)

    GET /sapi/v1/margin/myTrades

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-trade-list-user_data

    Args:
        symbol (str)
    Keyword Args:
        fromID (int, optional): TradeId to fetch from. Default gets most recent trades.
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 500.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    payload = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", "/sapi/v1/margin/myTrades", payload)


def margin_max_borrowable(self, asset: str, **kwargs):
    """Query Max Borrow (USER_DATA)

    GET /sapi/v1/margin/maxBorrowable

    https://binance-docs.github.io/apidocs/spot/en/#query-max-borrow-user_data

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/maxBorrowable", payload)


def margin_max_transferable(self, asset: str, **kwargs):
    """Query Max Transfer-Out Amount (USER_DATA)

    GET /sapi/v1/margin/maxTransferable

    https://binance-docs.github.io/apidocs/spot/en/#query-max-transfer-out-amount-user_data

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/maxBorrowable", payload)


def isolated_margin_transfer(
    self, asset: str, symbol: str, transFrom: str, transTo: str, amount, **kwargs
):
    """Isolated Margin Account Transfer (MARGIN)

    POST /sapi/v1/margin/isolated/transfer

    https://binance-docs.github.io/apidocs/spot/en/#isolated-margin-account-transfer-margin

    Args:
        asset (str)
        symbol (str)
        amount (float)
        transFrom (str): "SPOT", "ISOLATED_MARGIN"
        transTo (str): "SPOT", "ISOLATED_MARGIN"
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [asset, "asset"],
            [symbol, "symbol"],
            [transFrom, "transFrom"],
            [transTo, "transTo"],
            [amount, "amount"],
        ]
    )

    payload = {
        "asset": asset,
        "symbol": symbol,
        "transFrom": transFrom,
        "transTo": transTo,
        "amount": amount,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/margin/isolated/transfer", payload)


def isolated_margin_transfer_history(self, symbol: str, **kwargs):
    """Get Isolated Margin Transfer History (USER_DATA)

    GET /sapi/v1/margin/isolated/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-isolated-margin-transfer-history-user_data

    Args:
        symbol (str)
    Keyword Args:
        asset (str, optional): asset,such as BTC
        transFrom (str, optional): "SPOT", "ISOLATED_MARGIN"
        transTo (str, optional): "SPOT", "ISOLATED_MARGIN"
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/isolated/transfer", payload)


def isolated_margin_account(self, **kwargs):
    """Query Isolated Margin Account Info (USER_DATA)

    GET /sapi/v1/margin/isolated/account

    https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data

    Keyword Args:
        symbols (str, optional): Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/isolated/account", kwargs)


def isolated_margin_pair(self, symbol: str, **kwargs):
    """Query Isolated Margin Symbol (USER_DATA)

    GET /sapi/v1/margin/isolated/pair

    https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    payload = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", "/sapi/v1/margin/isolated/pair", payload)


def isolated_margin_all_pairs(self, **kwargs):
    """Get All Isolated Margin Symbol(USER_DATA)

    GET /sapi/v1/margin/isolated/allPairs

    https://binance-docs.github.io/apidocs/spot/en/#get-all-isolated-margin-symbol-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/isolated/allPairs", kwargs)


def toggle_bnbBurn(self, **kwargs):
    """Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)

    POST /sapi/v1/bnbBurn

    https://binance-docs.github.io/apidocs/spot/en/#toggle-bnb-burn-on-spot-trade-and-margin-interest-user_data

    Keyword Args:
        spotBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT
        interestBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for margin loan's interest
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/bnbBurn", kwargs)


def bnbBurn_status(self, **kwargs):
    """Get BNB Burn Status (USER_DATA)

    GET /sapi/v1/bnbBurn

    https://binance-docs.github.io/apidocs/spot/en/#get-bnb-burn-status-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/bnbBurn", kwargs)


def margin_interest_rate_history(self, asset: str, **kwargs):
    """Get Margin Interest Rate History (USER_DATA)

    GET /sapi/v1/margin/interestRateHistory

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-interest-rate-history-user_data

    Args:
        asset (str)
    Keyword Args:
        vipLevel (str, optional): Default: user's vip level
        startTime (int, optional): Default: 7 days ago.
        endTime (int, optional): Default: present. Maximum range: 3 months.
        limit (int, optional): Default: 20. Maximum: 100.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/interestRateHistory", payload)
