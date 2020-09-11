import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -1105, 'msg': 'error message.'}

key = random_str()
secret = random_str()

params = {
    'collateralCoin': 'BTC'
}


def test_futures_loan_calc_max_adjust_amount_without_collateral_coin():
    """ Tests the API endpoint to Adjust Cross-Collateral LTV without collateralCoin """

    params = {
        'collateralCoin': '',
    }
    client = Client(key, secret)
    client.futures_loan_calc_max_adjust_amount.when.called_with(
        **params).should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, '/sapi/v1/futures/loan/calcMaxAdjustAmount\\?' + urlencode(params), mock_item, 200)
def test_futures_loan_calc_max_adjust_amount():
    """ Tests the API endpoint to get Adjust Cross-Collateral LTV """

    client = Client(key, secret)
    response = client.futures_loan_calc_max_adjust_amount(**params)
    response.should.equal(mock_item)
