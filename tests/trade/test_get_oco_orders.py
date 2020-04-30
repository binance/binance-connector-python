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
    'fromId': '1234567',
    'startTime': timestamp(),
    'endTime': timestamp(),
    'limit': 10
}

@mock_http_response(responses.GET, '/api/v3/allOrderList', mock_item, 200)
def test_get_oco_orders_without_parameters():
    """ Tests the API endpoint to get oco orders without parameters """

    client =  binance.Trade(key, secret)
    response = client.get_oco_orders()
    response.should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/allOrderList\\?' + urlencode(params), mock_item, 200)
def test_get_oco_orders_with_parameters():
    """ Tests the API endpoint to get oco orders with provided parameters """

    client =  binance.Trade(key, secret)
    response = client.get_oco_orders(**params)
    response.should.equal(mock_item)