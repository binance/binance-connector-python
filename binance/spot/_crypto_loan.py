from binance.lib.utils import check_required_parameters, check_required_parameter


def loan_history(self, asset: str, **kwargs):
    """Get Crypto Loans Income History (USER_DATA)

    GET /sapi/v1/loan/income

    https://developers.binance.com/docs/crypto_loan/stable-rate/market-data/Get-Crypto-Loans-Income-History

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


def loan_borrow_history(self, **kwargs):
    """Get Loan Borrow History (USER_DATA)

    GET /sapi/v1/loan/borrow/history

    https://developers.binance.com/docs/crypto_loan/stable-rate/user-information/Get-Loan-Borrow-History

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


def loan_repay_history(self, **kwargs):
    """Get Loan Repayment History (USER_DATA)

    GET /sapi/v1/loan/repay/history

    https://developers.binance.com/docs/crypto_loan/stable-rate/user-information/Get-Loan-Repayment-History

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


def loan_adjust_ltv_history(self, **kwargs):
    """Get Loan LTV Adjustment History (USER_DATA)

    GET /sapi/v1/loan/ltv/adjustment/history

    https://developers.binance.com/docs/crypto_loan/stable-rate/user-information/Get-Loan-LTV-Adjustment-History

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

    https://developers.binance.com/docs/vip_loan/user-information/Get-VIP-Loan-Ongoing-Orders

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

    https://developers.binance.com/docs/vip_loan/trade/VIP-Loan-Repay

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

    https://developers.binance.com/docs/vip_loan/user-information/Get-VIP-Loan-Repayment-History

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

    https://developers.binance.com/docs/vip_loan/user-information/Check-Locked-Value-of-VIP-Collateral-Account

    Keyword Args:
      orderId (int, optional)
      collateralAccountId (int, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/vip/collateral/account", kwargs)


def loan_loanable_data(self, **kwargs):
    """Get Loanable Assets Data (USER_DATA)

    GET /sapi/v1/loan/loanable/data

    https://developers.binance.com/docs/vip_loan/market-data/Get-Loanable-Assets-Data

    Keyword Args:
      loanCoin (str, optional)
      vipLevel (int, optional)
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/loan/loanable/data", kwargs)
