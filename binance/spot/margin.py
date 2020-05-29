from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters

def margin_transfer(self, asset: str, amount: str, type: int, **kwargs):
    """ Margin Account Transfer (MARGIN)
    Execute transfer between spot account and margin account.

    POST /sapi/v1/margin/transfer

    https://binance-docs.github.io/apidocs/spot/en/#margin-account-transfer-margin

    """
    
    check_required_parameters([[asset, 'asset'], [amount, 'amount'], [type, 'type']])
    
    url_path = '/sapi/v1/margin/transfer'
    payload = {'asset': asset, 'amount': amount,  'type': type, **kwargs}
    return self.sign_request('POST', url_path, payload)
