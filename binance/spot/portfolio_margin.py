def portfolio_margin_account(self, **kwargs):
    """Get Portfolio Margin Account Info (USER_DATA)

    GET /sapi/v1/portfolio/account

    https://binance-docs.github.io/apidocs/spot/en/#get-portfolio-margin-account-info-user_data

    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/portfolio/account", {**kwargs})
