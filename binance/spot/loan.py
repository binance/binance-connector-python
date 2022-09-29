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
