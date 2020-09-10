import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -1105, 'msg': 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()


def test_new_isolate_margin_account_without_base():
    """ Tests the API endpoint to create isolated margin account without base """

    param = {
        'base': '',
        'quote': 'USDT'
    }
    client = Client(key, secret)
    client.new_isolate_margin_account.when.called_with(
        **param).should.throw(ParameterRequiredError)


def test_new_isolate_margin_account_without_quote():
    """ Tests the API endpoint to create isolated margin account without quote """

    param = {
        'base': 'BTC',
        'quote': ''
    }
    client = Client(key, secret)
    client.new_isolate_margin_account.when.called_with(
        **param).should.throw(ParameterRequiredError)


@mock_http_response(responses.POST, '/sapi/v1/margin/isolated/create\\?base=BTC&quote=USDT', mock_item, 200)
def test_new_isolate_margin_account():
    """ Tests the API endpoint to create isolated margin account """

    param = {
        'base': 'BTC',
        'quote': 'USDT'
    }
    client = Client(key, secret)
    response = client.new_isolate_margin_account(**param)
    response.should.equal(mock_item)
