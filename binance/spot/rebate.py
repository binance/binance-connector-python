def rebate_spot_history(self, **kwargs):
    """Get Spot Rebate History Records (USER_DATA)

    GET /sapi/v1/rebate/taxQuery

    https://binance-docs.github.io/apidocs/spot/en/#get-spot-rebate-history-records-user_data

    Keyword Args:
      startTime (int, optional)
      endTime (int, optional)
      page (int, optional): default 1
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/rebate/taxQuery", kwargs)
