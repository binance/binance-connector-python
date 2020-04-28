import sure
import binance
import responses

from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
key = random_str()
secret = random_str()

@mock_http_response(responses.GET, '/api/v3/account', mock_item, 200)
def test_account():
    """ Tests the API endpoint to account information  """

    client = binance.Trade(key, secret)
    response = client.account()
    response.should.equal(mock_item)
