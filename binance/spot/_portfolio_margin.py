from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def portfolio_margin_account(self, **kwargs):
    """Get Classic Portfolio Margin Account Info (USER_DATA)

    Get the account info

    'Weight(IP): 1'

    GET /sapi/v1/portfolio/account

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate

    """

    url_path = "/sapi/v1/portfolio/collateralRate"
    return self.sign_request("GET", url_path)


def portfolio_margin_tiered_collateral_rate(self, **kwargs):
    """Portfolio Margin Pro Tiered Collateral Rate (USER_DATA)

    Portfolio Margin PRO Tiered Collateral Rate

    Weight(IP): 50

    GET /sapi/v2/portfolio/collateralRate

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v2/portfolio/collateralRate"
    return self.sign_request("GET", url_path, {**kwargs})


def portfolio_margin_bankruptcy_loan_amount(self, **kwargs):
    """Query Classic Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

    Query Classic Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

    Weight(UID): 500

    GET /sapi/v1/portfolio/pmLoan

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History

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


def get_portfolio_margin_span_account_info(self, **kwargs):
    """Get Portfolio Margin Pro SPAN Account Info (USER_DATA)

    Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)

    Weight(IP): 5

    GET /sapi/v2/portfolio/account

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v2/portfolio/account"
    return self.sign_request("GET", url_path, {**kwargs})


def get_portfolio_margin_account_balance(self, **kwargs):
    """Get Portfolio Margin Pro Account Balance (USER_DATA)

    Query Portfolio Margin Pro account balance

    Weight(IP): 20

    GET /sapi/v1/portfolio/balance

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info

    Keyword Args:
        asset (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/portfolio/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def query_portfolio_margin_asset_index_price(self, **kwargs):
    """Query Portfolio Margin Asset Index Price (MARKET_DATA)

    Query Portfolio Margin Asset Index Price

    Weight(IP):
    - 1 if send asset
    - 50 if not send asset

    GET /sapi/v1/portfolio/asset-index-price

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Query-Portfolio-Margin-Asset-Index-Price

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/BNB-transfer

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance

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

    https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset

    Args:
        asset (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(asset, "asset")

    params = {"asset": asset, **kwargs}
    url_path = "/sapi/v1/portfolio/asset-collection"
    return self.sign_request("POST", url_path, params)
