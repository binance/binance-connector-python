import responses

from binance.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@mock_http_response(
    responses.GET, "/api/v3/openOrderList\\?recvWindow=1000", mock_item, 200
)
def test_get_oco_open_orders():
    """Tests the API endpoint to get all oco open orders"""

    client = Client(key, secret)
    response = client.get_oco_open_orders(recvWindow=1000)
    response.should.equal(mock_item)
