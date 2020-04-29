import sure
import binance
import responses

from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError, APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -2011,'msg': 'unknown order sent'}

key = random_str()
secret = random_str()

orderId= '1234567'
origClientOrderId = '2345678'

def test_cancel_open_orders_without_symbol():
    """ Tests the API endpoint to cancel all open orders without symbol """

    client =  binance.Trade(key, secret)
    client.cancel_open_orders.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.DELETE, '/api/v3/openOrders\\?symbol=ETHBTC', mock_exception, 400)
def test_cancel_open_orders_when_no_open_orders():
    """ Tests the API endpoint to cancel all open orders when there is no open order """

    client =  binance.Trade(key, secret)
    client.cancel_open_orders.when.called_with('ETHBTC').should.throw(APIException)

@mock_http_response(responses.DELETE, '/api/v3/openOrders\\?symbol=ETHBTC', mock_item, 200)
def test_cancel_open_orders():
    """ Tests the API endpoint to cancel all open orders """

    client =  binance.Trade(key, secret)
    response = client.cancel_open_orders('ETHBTC')
    response.should.equal(mock_item)
