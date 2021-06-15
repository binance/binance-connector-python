from binance.spot import Spot as Client
import responses

from tests.util import random_str
from tests.util import mock_http_response
from urllib.parse import urlencode

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"symbol": "BTCUSDT", "recvWindow": 1000}


@mock_http_response(responses.GET, "/api/v3/openOrders", mock_item, 200)
def test_get_open_orders_for_all_pairs():
    """Tests the API endpoint to get all open orders"""

    client = Client(key, secret)
    response = client.get_open_orders()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/openOrders\\?" + urlencode(params), mock_item, 200
)
def test_get_open_orders_for_one_pair():
    """Tests the API endpoint to get open orders for one pair"""

    client = Client(key, secret)
    response = client.get_open_orders(**params)
    response.should.equal(mock_item)
