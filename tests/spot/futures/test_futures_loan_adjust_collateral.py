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
    'collateralCoin': 'BNB',
    'amount': '1',
    'direction': 'ADDITIONAL'
}


def test_futures_loan_adjust_collateral_without_collateralCoin():
    """ Tests the API endpoint to Adjust Cross-Collateral LTV without collateralCoin """

    params = {
        'collateralCoin': '',
        'amount': '1',
        'direction': 'ADDITIONAL'
    }

    client = Client(key, secret)
    client.futures_loan_adjust_collateral.when.called_with(
        **params).should.throw(ParameterRequiredError)


def test_futures_loan_adjust_collateral_without_amount():
    """ TTests the API endpoint to Adjust Cross-Collateral LTV without collateralCoin """

    params = {
        'collateralCoin': 'BNB',
        'amount': '',
        'direction': 'ADDITIONAL'
    }
    client = Client(key, secret)
    client.futures_loan_adjust_collateral.when.called_with(
        **params).should.throw(ParameterRequiredError)


def test_futures_loan_adjust_collateral_without_direction():
    """ TTests the API endpoint to Adjust Cross-Collateral LTV without collateralCoin """

    params = {
        'collateralCoin': 'BNB',
        'amount': '1',
        'direction': ''
    }
    client = Client(key, secret)
    client.futures_loan_adjust_collateral.when.called_with(
        **params).should.throw(ParameterRequiredError)


@mock_http_response(responses.POST, '/sapi/v1/futures/loan/adjustCollateral\\?' + urlencode(params), mock_item, 200)
def test_futures_loan_adjust_collateral():
    """ Tests the API endpoint to Adjust Cross-Collateral LTV """

    client = Client(key, secret)
    response = client.futures_loan_adjust_collateral(**params)
    response.should.equal(mock_item)
