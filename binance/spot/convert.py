from binance.lib.utils import check_required_parameters


def convert_trade_history(self, startTime: int, endTime: int, **kwargs):
    """Convert Trade History (USER_DATA)

    Get convert history for a specific account.

    GET /sapi/v1/convert/tradeFlow

    https://binance-docs.github.io/apidocs/spot/en/#convert-endpoints

    Args:
        startTime (int)
        endTime (int)
    Keyword Args:
        limit (int, optional): Default Value: 100; Max Value: 1000
        recvWindow (int, optional)
    """
    check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

    url_path = "/sapi/v1/convert/tradeFlow"
    payload = {"startTime": startTime, "endTime": endTime, **kwargs}
    return self.sign_request("GET", url_path, payload)
