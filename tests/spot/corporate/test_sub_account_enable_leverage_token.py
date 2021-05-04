import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()

params = {
    'email': 'alice@test.com',
    'enableBlvt': True,
    'recvWindow': 1000
}

def test_sub_account_enable_leverage_token_without_params():
    """ Tests the API endpoint to enable leverage token for sub-account without params """
    params = {
        'email': None,
        'enableBlvt': None
    }
    client = Client(key, secret)
    client.sub_account_enable_leverage_token.when.called_with(**params).should.throw(ParameterRequiredError)


def test_sub_account_enable_leverage_token_without_email():
    """ Tests the API endpoint to enable leverage token for sub-account without email """
    params = {
        'email': '',
        'enableBlvt': True,
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_enable_leverage_token.when.called_with(**params).should.throw(ParameterRequiredError)


def test_sub_account_enable_leverage_token_without_enableBlvt():
    """ Tests the API endpoint to enable leverage token for sub-account without enableBlvt """
    params = {
        'email': 'alice@test.com',
        'enableBlvt': None,
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_enable_leverage_token.when.called_with(**params).should.throw(ParameterRequiredError)


@mock_http_response(responses.POST,
                    '/sapi/v1/sub-account/blvt/enable\\?' + encoded_string(params),
                    mock_item, 200)
def test_sub_account_enable_leverage_token():
    """ Tests the API endpoint to enable leverage for token sub-account """

    client = Client(key, secret)
    response = client.sub_account_enable_leverage_token(**params)
    response.should.equal(mock_item)
