from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def margin_transfer(self, asset: str, amount, type: int, **kwargs):
    """ Margin Account Transfer (MARGIN)
    Execute transfer between spot account and margin account.

    POST /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-transfer-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount'], [type, 'type']])

    url_path = '/sapi/v1/margin/transfer'
    payload = {'asset': asset, 'amount': amount, 'type': type, **kwargs}
    return self.sign_request('POST', url_path, payload)


def margin_borrow(self, asset: str, amount, **kwargs):
    """ Margin Account Borrow (MARGIN)
    Apply for a loan.

    POST /sapi/v1/margin/load

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-borrow-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount']])

    url_path = '/sapi/v1/margin/loan'
    payload = {'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', url_path, payload)


def margin_repay(self, asset: str, amount, **kwargs):
    """ Margin Account Repay(MARGIN)
    Repay loan for margin account.

    POST /sapi/v1/margin/repay

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-repay-margin

    """

    check_required_parameters([[asset, 'asset'], [amount, 'amount']])

    url_path = '/sapi/v1/margin/repay'
    payload = {'asset': asset, 'amount': amount, **kwargs}
    return self.sign_request('POST', url_path, payload)


def margin_asset(self, asset: str, **kwargs):
    """ Query Margin Asset (MARKET_DATA)

    GET /sapi/v1/margin/asset 

    https://binance-docs.github.io/apidocs/spot/en/#query-margin-asset-market_data

    """

    check_required_parameter(asset, 'asset')

    url_path = '/sapi/v1/margin/asset'
    payload = {'asset': asset, **kwargs}
    return self.limit_request('GET', url_path, payload)
