import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = [{"key_1": "value_1", "key_2": "value_2"}]
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/asset/wallet/balance", mock_item, 200)
def test_balance():
    """Tests the API endpoint to get balance"""

    client = Client(key, secret)
    response = client.balance()
    response.should.equal(mock_item)
