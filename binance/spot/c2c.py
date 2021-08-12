from binance.lib.utils import check_required_parameter


def c2c_trade_history(self, tradeType: str, **kwargs):
    """Get C2C Trade History (USER_DATA)

    GET /sapi/v1/c2c/orderMatch/listUserOrderHistory

    https://binance-docs.github.io/apidocs/spot/en/#get-c2c-trade-history-user_data

    Args:
      tradeType (str): BUY, SELL
    Keyword Args:
      startTimestamp (int, optional)
      endTimestamp (int, optional)
      page (int, optional): default 1
      rows (int, optional): default 100, max 100
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(tradeType, "tradeType")

    payload = {"tradeType": tradeType, **kwargs}
    return self.sign_request(
        "GET", "/sapi/v1/c2c/orderMatch/listUserOrderHistory", payload
    )
