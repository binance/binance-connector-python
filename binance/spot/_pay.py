def pay_history(self, **kwargs):
    """Get Pay Trade History (USER_DATA)

    GET /sapi/v1/pay/transactions

    https://binance-docs.github.io/apidocs/spot/en/#get-pay-trade-history-user_data

    Keyword Args:
      startTime (int, optional)
      endTime (int, optional)
      limit (int, optional): default 100, max 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/pay/transactions", kwargs)
