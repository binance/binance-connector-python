import sure
import binance
import responses

from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.error import APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -1,'msg': 'error message'}

key = random_str()
secret = random_str()

params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'quantity': 0.002,
    'price': 9500,
    'stopPrice': 7500,
    'stopLimitPrice': 7000,
    'stopLimitTimeInForce': 'GTC'
}

@mock_http_response(responses.POST, '/api/v3/order/oco', mock_exception, 400)
def test_post_an_oct_order_without_param():
    """ Tests the API endpoint to post a new oco order without parameters """

    client =  binance.Trade(key, secret)
    client.new_oco_order.when.called_with().should.throw(APIException)

@mock_http_response(responses.POST, '/api/v3/order/oco\\?' + urlencode(params), mock_item, 200)
def test_post_an_oct_order():
    """ Tests the API endpoint to post a new oco order """

    client =  binance.Trade(key, secret)
    response = client.new_oco_order(**params)
    response.should.equal(mock_item)
