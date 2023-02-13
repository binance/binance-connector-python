def portfolio_margin_account(self, **kwargs):
    """Get Portfolio Margin Account Info (USER_DATA)

    GET /sapi/v1/portfolio/account

    https://binance-docs.github.io/apidocs/spot/en/#get-portfolio-margin-account-info-user_data

    Keyword Args:
      recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/portfolio/account", {**kwargs})


def portfolio_margin_collateral_rate(self):
    """Portfolio Margin Collateral Rate (MARKET_DATA)

    Portfolio Margin Collateral Rate.

    Weight(IP): 50

    GET /sapi/v1/portfolio/collateralRate

    https://binance-docs.github.io/apidocs/spot/en/#portfolio-margin-collateral-rate-market_data

    """

    url_path = "/sapi/v1/portfolio/collateralRate"
    return self.sign_request("GET", url_path)


def portfolio_margin_bankruptcy_loan_amount(self, **kwargs):
    """Query Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

    Query Portfolio Margin Bankruptcy Loan Amount.

    Weight(UID): 500

    GET /sapi/v1/portfolio/pmLoan

    https://binance-docs.github.io/apidocs/spot/en/#query-portfolio-margin-bankruptcy-loan-amount-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/pmLoan"
    return self.sign_request("GET", url_path, {**kwargs})


def portfolio_margin_bankruptcy_loan_repay(self, **kwargs):
    """Portfolio Margin Bankruptcy Loan Repay (USER_DATA)

    Repay Portfolio Margin Bankruptcy Loan.

    Weight(UID): 3000

    POST /sapi/v1/portfolio/repay

    https://binance-docs.github.io/apidocs/spot/en/#portfolio-margin-bankruptcy-loan-repay-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/repay"
    return self.sign_request("POST", url_path, {**kwargs})
