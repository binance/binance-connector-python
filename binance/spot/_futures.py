from binance.lib.utils import check_required_parameters

"""
  Endpoints that for moving funds between spot and futures accounts.
  It's not for trading on futures.

"""


def futures_transfer(self, asset: str, amount: float, type: int, **kwargs):
    """New Future Account Transfer (USER_DATA)
    Execute transfer between spot account and futures account.

    POST /sapi/v1/futures/transfer

    https://binance-docs.github.io/apidocs/spot/en/#new-future-account-transfer-user_data

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
