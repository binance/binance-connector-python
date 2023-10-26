from binance.lib.utils import check_required_parameters, check_required_parameter


def loan_history(self, asset: str, **kwargs):
    """Get Crypto Loans Income History (USER_DATA)

    GET /sapi/v1/loan/income

    https://binance-docs.github.io/apidocs/spot/en/#get-crypto-loans-income-history-user_data

    Args:
      asset (str)
    Keyword Args:
      type (str, optional): All types will be returned by default.
                            borrowIn, collateralSpent, repayAmount, collateralReturn (collateral return after repayment),
                            addCollateral, removeCollateral, collateralReturnAfterLiquidation
      startTime (int, optional)
      endTime (int, optional)
      limit (int, optional): default 20, max 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")

    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/loan/income", payload)


def loan_borrow(self, loanCoin: str, collateralCoin: str, loanTerm: int, **kwargs):
    """Crypto Loan Borrow (TRADE)

    POST /sapi/v1/loan/borrow

    https://binance-docs.github.io/apidocs/spot/en/#borrow-crypto-loan-borrow-trade

    Args:
      loanCoin (str)
      collateralCoin (str)
      loanTerm (int): 7/14/30/90/180 days
    Keyword Args:
      loanAmount (float, optional): Mandatory when collateralAmount is empty
      collateralAmount (float, optional): Mandatory when loanAmount is empty
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [collateralCoin, "collateralCoin"],
            [loanTerm, "loanTerm"],
        ]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "loanTerm": loanTerm,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/loan/borrow", payload)


def loan_borrow_history(self, **kwargs):
    """Get Loan Borrow History (USER_DATA)

    GET /sapi/v1/loan/borrow/history

    https://binance-docs.github.io/apidocs/spot/en/#borrow-get-loan-borrow-history-user_data

    Keyword Args:
      orderId (int, optional): orderId in POST /sapi/v1/loan/borrow
      loanCoin (str, optional)
      collateralCoin (str, optional)
      startTime (int, optional)
      endTime (int, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000.
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/borrow/history", kwargs)


def loan_ongoing_orders(self, **kwargs):
    """Get Loan Ongoing Orders (USER_DATA)

    GET /sapi/v1/loan/ongoing/orders

    https://binance-docs.github.io/apidocs/spot/en/#borrow-get-loan-ongoing-orders-user_data

    Keyword Args:
      orderId (int, optional): orderId in POST /sapi/v1/loan/borrow
      loanCoin (str, optional)
      collateralCoin (str, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/ongoing/orders", kwargs)


def loan_repay(self, orderId: int, amount: float, **kwargs):
    """Crypto Loan Repay (TRADE)

    POST /sapi/v1/loan/repay

    https://binance-docs.github.io/apidocs/spot/en/#repay-crypto-loan-repay-trade

    Args:
      orderId (int)
      amount (float)
    Keyword Args:
      type (int, optional): Default: 1. 1 for "repay with borrowed coin"; 2 for "repay with collateral"
      collateralReturn (boolean, optional): Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra collateral in the order.
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[orderId, "orderId"], [amount, "amount"]])

    payload = {"orderId": orderId, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/loan/repay", payload)


def loan_repay_history(self, **kwargs):
    """Get Loan Repayment History (USER_DATA)

    GET /sapi/v1/loan/repay/history

    https://binance-docs.github.io/apidocs/spot/en/#repay-get-loan-repayment-history-user_data

    Keyword Args:
      orderId (int, optional)
      loanCoin (str, optional)
      collateralCoin (str, optional)
      startTime (int, optional)
      endTime (int, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000.
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/repay/history", kwargs)


def loan_adjust_ltv(self, orderId: int, amount: float, direction: str, **kwargs):
    """Crypto Loan Adjust LTV (TRADE)

    POST /sapi/v1/loan/adjust/ltv

    https://binance-docs.github.io/apidocs/spot/en/#adjust-ltv-crypto-loan-adjust-ltv-trade

    Args:
      orderId (int)
      amount (float)
      direction (str): "ADDITIONAL", "REDUCED"
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[orderId, "orderId"], [amount, "amount"], [direction, "direction"]]
    )

    payload = {"orderId": orderId, "amount": amount, "direction": direction, **kwargs}
    return self.sign_request("POST", "/sapi/v1/loan/adjust/ltv", payload)


def loan_adjust_ltv_history(self, **kwargs):
    """Get Loan LTV Adjustment History (USER_DATA)

    GET /sapi/v1/loan/ltv/adjustment/history

    https://binance-docs.github.io/apidocs/spot/en/#adjust-ltv-get-loan-ltv-adjustment-history-user_data

    Keyword Args:
      orderId (int, optional)
      loanCoin (str, optional)
      collateralCoin (str, optional)
      startTime (int, optional)
      endTime (int, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/ltv/adjustment/history", kwargs)


def loan_vip_ongoing_orders(self, **kwargs):
    """Get VIP Loan Ongoing Orders (USER_DATA)

    GET /sapi/v1/loan/vip/ongoing/orders

    https://binance-docs.github.io/apidocs/spot/en/#get-vip-loan-ongoing-orders-user_data

    Keyword Args:
      orderId (int, optional)
      collateralAccountId (int, optional)
      loanCoin (str, optional)
      collateralCoin (str, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/vip/ongoing/orders", kwargs)


def loan_vip_repay(self, orderId: int, amount: float, **kwargs):
    """VIP Loan Repay (TRADE)

    POST /sapi/v1/loan/vip/repay

    https://binance-docs.github.io/apidocs/spot/en/#vip-loan-repay-trade

    Args:
      orderId (int)
      amount (float)
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[orderId, "orderId"], [amount, "amount"]])

    payload = {"orderId": orderId, "amount": amount, **kwargs}
    return self.sign_request("POST", "/sapi/v1/loan/vip/repay", payload)


def loan_vip_repay_history(self, **kwargs):
    """Get VIP Loan Repayment History (USER_DATA)

    GET /sapi/v1/loan/vip/repay/history

    https://binance-docs.github.io/apidocs/spot/en/#get-vip-loan-repayment-history-user_data

    Keyword Args:
      orderId (int, optional)
      loanCoin (str, optional)
      startTime (int, optional)
      endTime (int, optional)
      current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
      limit (int, optional): Default: 10; max: 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/vip/repay/history", kwargs)


def loan_vip_collateral_account(self, **kwargs):
    """Check Locked Value of VIP Collateral Account (USER_DATA)

    GET /sapi/v1/loan/vip/collateral/account

    https://binance-docs.github.io/apidocs/spot/en/#check-locked-value-of-vip-collateral-account-user_data

    Keyword Args:
      orderId (int, optional)
      collateralAccountId (int, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/vip/collateral/account", kwargs)


def loan_loanable_data(self, **kwargs):
    """Get Loanable Assets Data (USER_DATA)

    GET /sapi/v1/loan/loanable/data

    https://binance-docs.github.io/apidocs/spot/en/#get-loanable-assets-data-user_data

    Keyword Args:
      loanCoin (str, optional)
      vipLevel (int, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/loanable/data", kwargs)


def loan_collateral_data(self, **kwargs):
    """Get Collateral Assets Data (USER_DATA)

    GET /sapi/v1/loan/collateral/data

    https://binance-docs.github.io/apidocs/spot/en/#get-collateral-assets-data-user_data

    Keyword Args:
      collateralCoin (str, optional)
      vipLevel (int, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/collateral/data", kwargs)


def loan_collateral_rate(
    self, loanCoin: str, collateralCoin: str, repayAmount: float, **kwargs
):
    """Check Collateral Repay Rate (USER_DATA)

    GET /sapi/v1/loan/repay/collateral/rate

    https://binance-docs.github.io/apidocs/spot/en/#check-collateral-repay-rate-user_data

    Args:
      loanCoin (str)
      collateralCoin (str)
      repayAmount (float)
    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [collateralCoin, "collateralCoin"],
            [repayAmount, "repayAmount"],
        ]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "repayAmount": repayAmount,
        **kwargs,
    }
    return self.sign_request("GET", "/sapi/v1/loan/repay/collateral/rate", payload)


def loan_customize_margin_call(self, marginCall: float, **kwargs):
    """Customize Margin Call (USER_DATA)

    POST /sapi/v1/loan/customize/margin_call

    https://binance-docs.github.io/apidocs/spot/en/#crypto-loan-customize-margin-call-trade

    Args:
      marginCall (float)
    Keyword Args:
      orderId (int, optional)
      collateralCoin (str, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(marginCall, "marginCall")

    payload = {"marginCall": marginCall, **kwargs}
    return self.sign_request("POST", "/sapi/v1/loan/customize/margin_call", payload)


def flexible_loan_borrow(self, loanCoin: str, collateralCoin: str, **kwargs):
    """Borrow - Flexible Loan Borrow (TRADE)

    Weight(UID): 6000

    POST /sapi/v1/loan/flexible/borrow

    https://binance-docs.github.io/apidocs/spot/en/#borrow-flexible-loan-borrow

    Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
    Keyword Args:
        loanAmount (float, optional): Loan amount
        collateralAmount (float, optional) Mandatory when loanAmount is empty
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[loanCoin, "loanCoin"], [collateralCoin, "collateralCoin"]]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        **kwargs,
    }

    url_path = "/sapi/v1/loan/flexible/borrow"
    return self.sign_request("POST", url_path, payload)


def flexible_loan_ongoing_orders(self, **kwargs):
    """Borrow - Get Flexible Loan Ongoing Orders (USER_DATA)

    Weight(IP): 300

    GET /sapi/v1/loan/flexible/ongoing/orders

    https://binance-docs.github.io/apidocs/spot/en/#borrow-get-flexible-loan-ongoing-orders-user_data

    Keyword Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
        current (int, optional): Current querying page. Start from 1. Default:1
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/ongoing/orders"
    return self.sign_request("GET", url_path, {**kwargs})


def flexible_loan_borrow_history(self, **kwargs):
    """Borrow - Get Flexible Loan Borrow History (USER_DATA)

    Weight(IP): 400

    GET /sapi/v1/loan/flexible/borrow/history

    https://binance-docs.github.io/apidocs/spot/en/#borrow-get-flexible-loan-borrow-history-user_data

    Keyword Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/borrow/history"
    return self.sign_request("GET", url_path, {**kwargs})


def flexible_loan_repay(
    self, loanCoin: str, collateralCoin: str, repayAmount: float, **kwargs
):
    """Repay - Flexible Loan Repay (TRADE)

    Weight(IP): 6000

    POST /sapi/v1/loan/flexible/repay

    https://binance-docs.github.io/apidocs/spot/en/#repay-flexible-loan-repay-trade

    Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
        repayAmount (float)
    Keyword Args:
        collateralReturn (boolean, optional)
        fullRepayment (boolean, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [repayAmount, "repayAmount"],
            [collateralCoin, "collateralCoin"],
            [loanCoin, "loanCoin"],
        ]
    )

    payload = {
        "repayAmount": repayAmount,
        "collateralCoin": collateralCoin,
        "loanCoin": loanCoin,
        **kwargs,
    }
    url_path = "/sapi/v1/loan/flexible/repay"
    return self.sign_request("POST", url_path, payload)


def flexible_loan_repayment_history(self, **kwargs):
    """Repay - Get Flexible Loan Repayment History (USER_DATA)


    Weight(IP): 400

    GET /sapi/v1/loan/flexible/repay/history

    https://binance-docs.github.io/apidocs/spot/en/#repay-get-flexible-loan-repayment-history-user_data

    Keyword Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/repay/history"
    return self.sign_request("GET", url_path, {**kwargs})


def flexible_loan_adjust_ltv(
    self,
    loanCoin: str,
    collateralCoin: str,
    adjustmentAmount: float,
    direction: str,
    **kwargs
):
    """Adjust LTV - Flexible Loan Adjust LTV (TRADE)


    Weight(UID): 6000

    POST /sapi/v1/loan/flexible/adjust/ltv

    https://binance-docs.github.io/apidocs/spot/en/#adjust-ltv-flexible-loan-adjust-ltv-trade

    Args:
        loanCoin (str)
        collateralCoin (str)
        adjustmentAmount (float)
        direction (Direction)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [collateralCoin, "collateralCoin"],
            [adjustmentAmount, "adjustmentAmount"],
            [direction, "direction"],
        ]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "adjustmentAmount": adjustmentAmount,
        "direction": direction,
        **kwargs,
    }
    url_path = "/sapi/v1/loan/flexible/adjust/ltv"
    return self.sign_request("POST", url_path, payload)


def flexible_loan_ltv_adjustment_history(self, **kwargs):
    """Adjust LTV - Get Flexible Loan LTV Adjustment History (USER_DATA)

    Weight(IP): 400

    GET /sapi/v1/loan/flexible/ltv/adjustment/history

    https://binance-docs.github.io/apidocs/spot/en/#adjust-ltv-get-flexible-loan-ltv-adjustment-history-user_data

    Keyword Args:
        loanCoin (str, optional): Coin loaned
        collateralCoin (str, optional): Coin used as collateral
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/ltv/adjustment/history"
    return self.sign_request("GET", url_path, {**kwargs})


def flexible_loan_assets_data(self, **kwargs):
    """Get Flexible Loan Assets Data (USER_DATA)

    Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

    Weight(IP): 400

    GET /sapi/v1/loan/flexible/loanable/data

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-loan-assets-data-user_data

    Keyword Args:
        loanCoin (str, optional): Coin loaned
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/loanable/data"
    return self.sign_request("GET", url_path, {**kwargs})


def flexible_loan_collateral_assets_data(self, **kwargs):
    """Get Flexible Loan Collateral Assets Data (USER_DATA)

    Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown in USD value.

    Weight(IP): 400

    GET /sapi/v1/loan/flexible/collateral/data

    https://binance-docs.github.io/apidocs/spot/en/#get-flexible-loan-collateral-assets-data-user_data

    Keyword Args:
        collateralCoin (str, optional): Coin used as collateral
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/loan/flexible/collateral/data"
    return self.sign_request("GET", url_path, {**kwargs})
