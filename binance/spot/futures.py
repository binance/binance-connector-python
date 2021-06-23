from binance.lib.utils import check_required_parameters

"""
  Endpoints that for moving funds between spot and futures accounts.
  It's not for trading on futures.

"""


def futures_transfer(self, asset: str, amount: float, type: int, **kwargs):
    """New Future Account Transfer (USER_DATA)
    Execute transfer between spot account and futures account.

    POST /sapi/v1/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#new-future-account-transfer-futures

    Args:
        asset (str): The asset being transferred, e.g. USDT
        amount (float): The amount to be transferred
        type (int): 1: transfer from spot account to USDT-Ⓜ futures account.
              2: transfer from USDT-Ⓜ futures account to spot account.
              3: transfer from spot account to COIN-Ⓜ futures account.
              4: transfer from COIN-Ⓜ futures account to spot account.
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [amount, "amount"], [type, "type"]])

    payload = {"asset": asset, "amount": amount, "type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/futures/transfer", payload)


def futures_transfer_history(self, asset: str, startTime, **kwargs):
    """Get Future Account Transaction History List (USER_DATA)

    GET /sapi/v1/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#get-future-account-transaction-history-list-user_data

    Args:
        asset (str): The asset being transferred, e.g. USDT
        startTime (int)
    Keyword Args:
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[asset, "asset"], [startTime, "startTime"]])

    payload = {"asset": asset, "startTime": startTime, **kwargs}
    return self.sign_request("GET", "/sapi/v1/futures/transfer", payload)


def futures_loan_borrow(self, coin: str, collateralCoin: str, **kwargs):
    """Borrow For Cross-Collateral (TRADE)

    POST /sapi/v1/futures/loan/borrow

    https://binance-docs.github.io/apidocs/spot/en/#borrow-for-cross-collateral-trade

    Args:
        coin (str)
        collateralCoin (str)
    Keyword Args:
        amount (float, optional): mandatory when collateralAmount is empty
        collateralAmount (float, optional): mandatory when amount is empty
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[coin, "coin"], [collateralCoin, "collateralCoin"]])

    payload = {"coin": coin, "collateralCoin": collateralCoin, **kwargs}
    return self.sign_request("POST", "/sapi/v1/futures/loan/borrow", payload)


def futures_loan_borrow_history(self, **kwargs):
    """Cross-Collateral Borrow History (USER_DATA)

    GET /sapi/v1/futures/loan/borrow/history

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-borrow-history-user_data

    Keyword Args:
        coin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 500, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/futures/loan/borrow/history", kwargs)


def futures_loan_repay(self, coin: str, collateralCoin: str, amount: float, **kwargs):
    """Repay For Cross-Collateral (TRADE)

    POST /sapi/v1/futures/loan/repay

    https://binance-docs.github.io/apidocs/spot/en/#repay-for-cross-collateral-trade

    Args:
        coin (str)
        collateralCoin (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[coin, "coin"], [collateralCoin, "collateralCoin"], [amount, "amount"]]
    )

    payload = {
        "coin": coin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/futures/loan/repay", payload)


def futures_loan_repay_history(self, **kwargs):
    """Cross-Collateral Repayment History (USER_DATA)

    GET /sapi/v1/futures/loan/repay/history

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-repayment-history-user_data

    Keyword Args:
        coin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 500, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/futures/loan/repay/history", kwargs)


def futures_loan_wallet(self, **kwargs):
    """Cross-Collateral Wallet (USER_DATA)

    GET /sapi/v2/futures/loan/wallet

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-wallet-v2-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v2/futures/loan/wallet", kwargs)


def futures_loan_configs(self, **kwargs):
    """Cross-Collateral Information (USER_DATA)

    GET /sapi/v2/futures/loan/configs

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-information-v2-user_data

    Keyword Args:
        loanCoin (str, optional)
        collateralCoin (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v2/futures/loan/configs", kwargs)


def futures_loan_calc_adjust_level(
    self, loanCoin: str, collateralCoin: str, amount: float, direction: str, **kwargs
):
    """Calculate Rate After Adjust Cross-Collateral LTV (USER_DATA)

    GET /sapi/v2/futures/loan/calcAdjustLevel

    https://binance-docs.github.io/apidocs/spot/en/#calculate-rate-after-adjust-cross-collateral-ltv-user_data

    Args:
        loanCoin (str)
        collateralCoin (str)
        amount (float)
        direction (str): "ADDITIONAL", "REDUCED"
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [collateralCoin, "collateralCoin"],
            [amount, "amount"],
            [direction, "direction"],
        ]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction,
        **kwargs,
    }

    return self.sign_request("GET", "/sapi/v2/futures/loan/calcAdjustLevel", payload)


def futures_loan_calc_max_adjust_amount(
    self, loanCoin: str, collateralCoin: str, **kwargs
):
    """Get Max Amount for Adjust Cross-Collateral LTV (USER_DATA)

    GET /sapi/v2/futures/loan/calcMaxAdjustAmount

    https://binance-docs.github.io/apidocs/spot/en/#get-max-amount-for-adjust-cross-collateral-ltv-v2-user_data

    Args:
        loanCoin (str)
        collateralCoin (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[loanCoin, "loanCoin"], [collateralCoin, "collateralCoin"]]
    )

    payload = {"loanCoin": loanCoin, "collateralCoin": collateralCoin, **kwargs}

    return self.sign_request(
        "GET", "/sapi/v2/futures/loan/calcMaxAdjustAmount", payload
    )


def futures_loan_adjust_collateral(
    self, loanCoin: str, collateralCoin: str, amount: float, direction: str, **kwargs
):
    """Adjust Cross-Collateral LTV (TRADE)

    POST /sapi/v2/futures/loan/adjustCollateral

    https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-v2-trade

    Args:
        loanCoin (str)
        collateralCoin (str)
        amount (float)
        direction (str): "ADDITIONAL", "REDUCED"
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [loanCoin, "loanCoin"],
            [collateralCoin, "collateralCoin"],
            [amount, "amount"],
            [direction, "direction"],
        ]
    )

    payload = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction,
        **kwargs,
    }

    return self.sign_request("POST", "/sapi/v2/futures/loan/adjustCollateral", payload)


def futures_loan_adjust_collateral_history(self, **kwargs):
    """Adjust Cross-Collateral LTV History (USER_DATA)

    GET /sapi/v1/futures/loan/adjustCollateral/history

    https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-history-user_data

    Keyword Args:
        loanCoin (str, optional)
        collateralCoin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 500, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request(
        "GET", "/sapi/v1/futures/loan/adjustCollateral/history", kwargs
    )


def futures_loan_liquidation_history(self, **kwargs):
    """Cross-Collateral Liquidation History (USER_DATA)

    GET /sapi/v1/futures/loan/liquidationHistory

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-liquidation-history-user_data

    Keyword Args:
        loanCoin (str, optional)
        collateralCoin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default 500, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/futures/loan/liquidationHistory", kwargs)


def futures_loan_collateral_repay_limit(self, coin: str, collateralCoin: str, **kwargs):
    """Check Collateral Repay Limit (USER_DATA)

    GET /sapi/v1/futures/loan/collateralRepayLimit

    https://binance-docs.github.io/apidocs/spot/en/#check-collateral-repay-limit-user_data

    Args:
        coin (str)
        collateralCoin (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[coin, "coin"], [collateralCoin, "collateralCoin"]])

    payload = {"coin": coin, "collateralCoin": collateralCoin, **kwargs}

    return self.sign_request(
        "GET", "/sapi/v1/futures/loan/collateralRepayLimit", payload
    )


def futures_loan_collateral_repay_quote(
    self, coin: str, collateralCoin: str, amount, **kwargs
):
    """Get Collateral Repay Quote (USER_DATA)

    GET /sapi/v1/futures/loan/collateralRepay

    https://binance-docs.github.io/apidocs/spot/en/#get-collateral-repay-quote-user_data

    Args:
        coin (str)
        collateralCoin (str)
        amount (float): repay amount
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [[coin, "coin"], [collateralCoin, "collateralCoin"], [amount, "amount"]]
    )

    payload = {
        "coin": coin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        **kwargs,
    }

    return self.sign_request("GET", "/sapi/v1/futures/loan/collateralRepay", payload)


def futures_loan_collateral_repay(self, quoteId: str, **kwargs):
    """Repay with Collateral (USER_DATA)

    POST /sapi/v1/futures/loan/collateralRepay

    https://binance-docs.github.io/apidocs/spot/en/#repay-with-collateral-user_data

    Args:
        quoteId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[quoteId, "quoteId"]])

    payload = {"quoteId": quoteId, **kwargs}

    return self.sign_request("POST", "/sapi/v1/futures/loan/collateralRepay", payload)


def futures_loan_collateral_repay_result(self, quoteId: str, **kwargs):
    """Collateral Repayment Result (USER_DATA)

    GET /sapi/v1/futures/loan/collateralRepayResult

    https://binance-docs.github.io/apidocs/spot/en/#collateral-repayment-result-user_data

    Args:
        quoteId (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[quoteId, "quoteId"]])

    payload = {"quoteId": quoteId, **kwargs}

    return self.sign_request(
        "GET", "/sapi/v1/futures/loan/collateralRepayResult", payload
    )


def futures_loan_interest_history(self, **kwargs):
    """Cross-Collateral Interest History (USER_DATA)

    GET /sapi/v1/futures/loan/interestHistory

    https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-interest-history-user_data

    Keyword Args:
        collateralCoin (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        limit (int, optional): default 500, max 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/futures/loan/interestHistory", kwargs)
