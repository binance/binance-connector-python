import sure
import binance
import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.error import APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -1, 'msg': 'error message'}

key = random_str()
secret = random_str()

params = {
    'symbol': 'BTCUSDT',
    'orderListId': random_str(),
    'origClientOrderId': random_str(),
    'recvWindow': 1000
}


@mock_http_response(responses.GET, '/api/v3/orderList', mock_exception, 400)
def test_get_oct_order_without_id():
    """ Tests the API endpoint to get oco order without given order id """

    client = binance.Trade(key, secret)
    client.get_oco_order.when.called_with().should.throw(APIException)


@mock_http_response(responses.GET, '/api/v3/orderList\\?orderListId=', mock_exception, 400)
def test_get_oct_order_with_empty_id():
    """ Tests the API endpoint to get order with empty order id """

    client = binance.Trade(key, secret)
    client.get_oco_order.when.called_with(
        orderListId='').should.throw(APIException)


@mock_http_response(responses.GET, '/api/v3/orderList\\?', mock_item, 200)
def test_get_order_with_order_id():
    """ Tests the API endpoint to get order """

    client = binance.Trade(key, secret)
    response = client.get_oco_order(**params)
    response.should.equal(mock_item)
