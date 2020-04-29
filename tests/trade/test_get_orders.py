import sure
import binance
import responses

from urllib.parse import urlencode
from tests.util import timestamp
from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError, APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()

params = {
    'orderId': '1234567',
    'origClientOrderId': '234567',
    'startTime': timestamp(),
    'endTime': timestamp()
}

def test_get_orders_without_symbol():
    """ Tests the API endpoint to get all orders without symbol """

    client =  binance.Trade(key, secret)
    client.get_orders.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/allOrders\\?symbol=ETHBTC', mock_item, 200)
def test_get_orders():
    """ Tests the API endpoint to get orders """

    client =  binance.Trade(key, secret)
    response = client.get_orders('ETHBTC')

@mock_http_response(responses.GET, '/api/v3/allOrders\\?symbol=ETHBTC&'+urlencode(params), mock_item, 200)
def test_get_orders_with_available_params():
    """ Tests the API endpoint to get orders based on parameters """

    client =  binance.Trade(key, secret)
    response = client.get_orders(symbol='ETHBTC', **params)
    response.should.equal(mock_item)
