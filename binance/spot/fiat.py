from binance.lib.utils import check_required_parameter


def fiat_order_history(self, transactionType: int, **kwargs):
    """Get Fiat Deposit/Withdraw History (USER_DATA)

    GET /sapi/v1/fiat/orders

    https://binance-docs.github.io/apidocs/spot/en/#get-fiat-deposit-withdraw-history-user_data

    Args:
      transactionType (int): 0-deposit,1-withdraw
    Keyword Args:
      beginTime (int, optional)
      endTime (int, optional)
      page (int, optional): default 1
      rows (int, optional): default 100, max 500
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(transactionType, "transactionType")
    payload = {"transactionType": transactionType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/fiat/orders", payload)


def fiat_payment_history(self, transactionType: int, **kwargs):
    """Get Fiat Payments History (USER_DATA)

    GET /sapi/v1/fiat/payments

    https://binance-docs.github.io/apidocs/spot/en/#get-fiat-payments-history-user_data

    Args:
      transactionType (int): 0-buy,1-sell
    Keyword Args:
      beginTime (int, optional)
      endTime (int, optional)
      page (int, optional): default 1
      rows (int, optional): default 100, max 500
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(transactionType, "transactionType")
    payload = {"transactionType": transactionType, **kwargs}
    return self.sign_request("GET", "/sapi/v1/fiat/payments", payload)
