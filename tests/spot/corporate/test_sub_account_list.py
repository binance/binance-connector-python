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

orderId = '1234567'
origClientOrderId = '2345678'

params = {
    # 'email': 'alice@test.com',
    'status': 'enabled',
    'page': 1,
    'limit': 100,
    'recvWindow': 1000
}


@mock_http_response(responses.GET, '/wapi/v3/sub-account/list.html\\?email=alice@test.com&' + urlencode(params), mock_item, 200)
def test_sub_account_list():
    """ Tests the API endpoint to query sub account list """

    client = Client(key, secret)
    response = client.sub_account_list(email='alice@test.com', **params)
    response.should.equal(mock_item)
