from binance.lib.utils import check_required_parameter, check_required_parameters


def vip_loan_borrow_interest_rate(self, loanCoin: str, **kwargs):
    """Get Borrow Interest Rate (USER_DATA)

    GET /sapi/v1/loan/vip/request/interestRate

    https://developers.binance.com/docs/vip_loan/market-data

    Args:
        loanCoin (str): Max 10 assets, Multiple split by ","
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(loanCoin, "loanCoin")
    payload = {"loanCoin": loanCoin, **kwargs}
    return self.sign_request("GET", "/sapi/v1/loan/vip/request/interestRate", payload)


def vip_loan_interest_rate_history(self, **kwargs):
    """Get VIP Loan Interest Rate History (USER_DATA)

    GET /sapi/v1/loan/vip/interest/history

    https://developers.binance.com/docs/vip_loan/market-data/Get-VIP-Loan-Interest-Rate-History

    Keyword Args:
        loanCoin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
        limit (int, optional): Default: 10; max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/interest/history", kwargs)


def vip_loan_loanable_data(self, **kwargs):
    """Get Loanable Assets Data (USER_DATA)

    GET /sapi/v1/loan/vip/loanable/data

    https://developers.binance.com/docs/vip_loan/market-data/Get-Loanable-Assets-Data

    Keyword Args:
        loanCoin (str, optional)
        vipLevel (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/loanable/data", kwargs)


def vip_loan_collateral_data(self, **kwargs):
    """Get Collateral Asset Data (USER_DATA)

    GET /sapi/v1/loan/vip/collateral/data

    https://developers.binance.com/docs/vip_loan/market-data/Get-Collateral-Asset-Data

    Keyword Args:
        collateralCoin (str, optional)
        vipLevel (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/collateral/data", kwargs)


def vip_loan_ongoing_orders(self, **kwargs):
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


def vip_loan_repayment_history(self, **kwargs):
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


def vip_loan_accrued_interest(self, **kwargs):
    """Get VIP Loan Accrued Interest (USER_DATA)

    GET /sapi/v1/loan/vip/accrual

    https://developers.binance.com/docs/vip_loan/user-information/Get-VIP-Loan-Accrued-Interest

    Keyword Args:
        orderId (int, optional)
        loanCoin (str, optional)
        collateralAccountId (int, optional)
        current (int, optional): Current querying page. Start from 1; default: 1; max: 1000
        limit (int, optional): Default: 10; max: 100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/accrual", kwargs)


def vip_loan_collateral_account(self, **kwargs):
    """Check Locked Value of VIP Collateral Account (USER_DATA)

    GET /sapi/v1/loan/vip/collateral/account

    https://developers.binance.com/docs/vip_loan/user-information/Check-Locked-Value-of-VIP-Collateral-Account

    Keyword Args:
        orderId (int, optional)
        collateralAccountId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/collateral/account", kwargs)


def vip_loan_application_status(self, **kwargs):
    """Query Application Status (USER_DATA)

    GET /sapi/v1/loan/vip/application/status

    https://developers.binance.com/docs/vip_loan/user-information/Query-Application-Status

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/loan/vip/application/status", kwargs)


def vip_loan_renew(self, orderId: int, **kwargs):
    """VIP Loan Renew (TRADE)

    POST /sapi/v1/loan/vip/renew

    https://developers.binance.com/docs/vip_loan/trade/VIP-Loan-Renew

    Args:
        orderId (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(orderId, "orderId")
    payload = {"orderId": orderId, **kwargs}
    return self.sign_request("POST", "/sapi/v1/loan/vip/renew", payload)


def vip_loan_repay(self, orderId: int, amount: float, **kwargs):
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


def vip_loan_borrow(
    self, loanCoin: str, loanAmount: float, collateralAccountId: int, **kwargs
):
    """VIP Loan Borrow (TRADE)

    POST /sapi/v1/loan/vip/borrow

    https://developers.binance.com/docs/vip_loan/trade/VIP-Loan-Borrow

    Args:
        loanCoin (str)
        loanAmount (float)
        collateralAccountId (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [loanAmount, "loanAmount"],
            [collateralAccountId, "collateralAccountId"],
        ]
    )
    payload = {
        "loanCoin": loanCoin,
        "loanAmount": loanAmount,
        "collateralAccountId": collateralAccountId,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/loan/vip/borrow", payload)
