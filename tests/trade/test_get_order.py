import sure
import binance
import responses

from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError, APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -2013,'msg': 'Order does not exist'}

key = random_str()
secret = random_str()

orderId= '1234567'
origClientOrderId = '2345678'

def test_get_order_without_symbol():
    """ Tests the API endpoint to get order without symbol """

    client =  binance.Trade(key, secret)
    client.get_order.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/order\\?symbol=ETHBTC&orderId=', mock_exception, 400)
def test_get_order_without_order_id():
    """ Tests the API endpoint to get order without provide order id """

    client =  binance.Trade(key, secret)
    client.get_order.when.called_with('ETHBTC', orderId='').should.throw(APIException)

@mock_http_response(responses.GET, '/api/v3/order\\?symbol=ETHBTC&orderId='+orderId, mock_item, 200)
def test_get_order_with_order_id():
    """ Tests the API endpoint to get order """

    client =  binance.Trade(key, secret)
    response = client.get_order('ETHBTC', orderId=orderId)
    response.should.equal(mock_item)
