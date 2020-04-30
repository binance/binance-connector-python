import sure
import binance
import responses

from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError, APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()

@mock_http_response(responses.GET, '/api/v3/openOrderList', mock_item, 200)
def test_get_oco_open_orders():
    """ Tests the API endpoint to get all oco open orders """

    client =  binance.Trade(key, secret)
    response = client.get_oco_open_orders()
    response.should.equal(mock_item)
