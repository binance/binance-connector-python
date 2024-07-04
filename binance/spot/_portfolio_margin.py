from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def portfolio_margin_account(self, **kwargs):
    """Get Classic Portfolio Margin Account Info (USER_DATA)

    Get the account info

    'Weight(IP): 1'

    GET /sapi/v1/portfolio/account

    https://binance-docs.github.io/apidocs/spot/en/#get-portfolio-margin-pro-account-info-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/account"
    return self.sign_request("GET", url_path, {**kwargs})


def portfolio_margin_collateral_rate(self):
    """Portfolio Margin Collateral Rate (MARKET_DATA)

    Portfolio Margin Collateral Rate.

    Weight(IP): 50

    GET /sapi/v1/portfolio/collateralRate

    https://binance-docs.github.io/apidocs/spot/en/#portfolio-margin-pro-collateral-rate-market_data

    """

    url_path = "/sapi/v1/portfolio/collateralRate"
    return self.sign_request("GET", url_path)


def portfolio_margin_bankruptcy_loan_amount(self, **kwargs):
    """Query Classic Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

    Query Classic Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

    Weight(UID): 500

    GET /sapi/v1/portfolio/pmLoan

    https://binance-docs.github.io/apidocs/spot/en/#query-portfolio-margin-pro-bankruptcy-loan-amount-user_data

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

    https://binance-docs.github.io/apidocs/spot/en/#portfolio-margin-pro-bankruptcy-loan-repay

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/repay"
    return self.sign_request("POST", url_path, {**kwargs})


def query_classic_portfolio_margin_negative_balance_interest_history(
    self, asset: str, **kwargs
):
    """Query Classic Portfolio Margin Negative Balance Interest History (USER_DATA)

    Query interest history of negative balance for portfolio margin.

    Weight(IP): 50

    GET /sapi/v1/portfolio/interest-history

    https://binance-docs.github.io/apidocs/spot/en/#query-portfolio-margin-pro-negative-balance-interest-history-user_data

    Args:
        asset (str)
    Keyword Args:
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(asset, "asset")

    params = {"asset": asset, **kwargs}
    url_path = "/sapi/v1/portfolio/interest-history"
    return self.sign_request("GET", url_path, params)


def query_portfolio_margin_asset_index_price(self, **kwargs):
    """Query Portfolio Margin Asset Index Price (MARKET_DATA)

    Query Portfolio Margin Asset Index Price

    Weight(IP):
    - 1 if send asset
    - 50 if not send asset

    GET /sapi/v1/portfolio/asset-index-price

    https://binance-docs.github.io/apidocs/spot/en/#query-portfolio-margin-asset-index-price-market_data

    Keyword Args:
        asset (str, optional)
    """

    url_path = "/sapi/v1/portfolio/asset-index-price"
    return self.limit_request("GET", url_path, kwargs)


def fund_auto_collection(self, **kwargs):
    """Fund Auto-collection (USER_DATA)

    Transfers all assets from Futures Account to Margin account

    Weight(IP): 1500

    POST /sapi/v1/portfolio/auto-collection

    https://binance-docs.github.io/apidocs/spot/en/#fund-auto-collection-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/auto-collection"
    return self.sign_request("POST", url_path, {**kwargs})


def bnb_transfer(self, transferSide: str, amount: float, **kwargs):
    """BNB Transfer (USER_DATA)

    BNB transfer can be between Margin Account and USDM Account

    Weight(IP): 1500

    POST /sapi/v1/portfolio/bnb-transfer

    https://binance-docs.github.io/apidocs/spot/en/#bnb-transfer-user_data

    Args:
        transferSide (str)
        amount (float)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[transferSide, "transferSide"], [amount, "amount"]])

    params = {"transferSide": transferSide, "amount": amount, **kwargs}
    url_path = "/sapi/v1/portfolio/bnb-transfer"
    return self.sign_request("POST", url_path, params)


def change_auto_repay_futures_status(self, autoRepay: bool, **kwargs):
    """Change Auto-repay-futures Status (TRADE)

    Change Auto-repay-futures Status

    Weight(IP): 1500

    POST /sapi/v1/portfolio/repay-futures-switch

    https://binance-docs.github.io/apidocs/spot/en/#change-auto-repay-futures-status-trade

    Args:
        autoRepay (boolean)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(autoRepay, "autoRepay")

    params = {"autoRepay": autoRepay, **kwargs}
    url_path = "/sapi/v1/portfolio/repay-futures-switch"
    return self.sign_request("POST", url_path, params)


def get_auto_repay_futures_status(self, **kwargs):
    """Get Auto-repay-futures Status (USER_DATA)

    Query Auto-repay-futures Status

    Weight(IP): 30

    GET /sapi/v1/portfolio/repay-futures-switch

    https://binance-docs.github.io/apidocs/spot/en/#get-auto-repay-futures-status-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/repay-futures-switch"
    return self.sign_request("GET", url_path, {**kwargs})


def repay_futures_negative_balance(self, **kwargs):
    """Repay futures Negative Balance (USER_DATA)

    Repay futures Negative Balance

    Weight(IP): 1500

    POST /sapi/v1/portfolio/repay-futures-negative-balance

    https://binance-docs.github.io/apidocs/spot/en/#repay-futures-negative-balance-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/portfolio/repay-futures-negative-balance"
    return self.sign_request("POST", url_path, {**kwargs})


def fund_collection_by_asset(self, asset: str, **kwargs):
    """Fund Collection by Asset (USER_DATA)

    Transfers specific asset from Futures Account to Margin account

    Weight(IP): 60

    POST /sapi/v1/portfolio/asset-collection

    https://binance-docs.github.io/apidocs/spot/en/#fund-collection-by-asset-user_data

    Args:
        asset (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(asset, "asset")

    params = {"asset": asset, **kwargs}
    url_path = "/sapi/v1/portfolio/asset-collection"
    return self.sign_request("POST", url_path, params)
