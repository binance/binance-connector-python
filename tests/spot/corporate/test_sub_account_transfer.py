import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()


params = {
    'fromEmail': 'alice@test.com',
    'toEmail': 'bob@test.com',
    'asset': 'BNB',
    'amount': 100,
    'recvWindow': 1000
}


def test_sub_account_transfer_without_fromEmail():
    """ Tests the API endpoint to sub account transfer without fromEmail """

    params = {
        'fromEmail': '',
        'toEmail': 'bob@test.com',
        'asset': 'BNB',
        'amount': 100,
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_transfer.when.called_with(
        **params).should.throw(ParameterRequiredError)


def test_sub_account_transfer_without_toEmail():
    """ Tests the API endpoint to sub account transfer without toEmail """

    params = {
        'fromEmail': 'alice@test.com',
        'toEmail': '',
        'asset': 'BNB',
        'amount': 100,
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_transfer.when.called_with(
        **params).should.throw(ParameterRequiredError)


def test_sub_account_transfer_without_asset():
    """ Tests the API endpoint to sub account transfer without asset """

    params = {
        'fromEmail': 'alice@test.com',
        'toEmail': 'bob@test.com',
        'asset': '',
        'amount': 100,
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_transfer.when.called_with(
        **params).should.throw(ParameterRequiredError)


def test_sub_account_transfer_without_amount():
    """ Tests the API endpoint to sub account transfer without amount """

    params = {
        'fromEmail': 'alice@test.com',
        'toEmail': 'bob@test.com',
        'asset': 'BNB',
        'amount': '',
        'recvWindow': 1000
    }
    client = Client(key, secret)
    client.sub_account_transfer.when.called_with(
        **params).should.throw(ParameterRequiredError)


@mock_http_response(responses.POST, '/wapi/v3/sub-account/transfer.html\\?' + encoded_string(params), mock_item, 200)
def test_sub_account_transfer():
    """ Tests the API endpoint to get transfer history """

    client = Client(key, secret)
    response = client.sub_account_transfer(**params)
    response.should.equal(mock_item)
