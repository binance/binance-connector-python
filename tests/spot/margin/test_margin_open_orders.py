import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"symbol": "BNBUSDT", "recvWindow": 1000}


@mock_http_response(
    responses.GET, "/sapi/v1/margin/openOrders\\?" + urlencode(params), mock_item, 200
)
def test_margin_open_orders():
    """Tests the API endpoint to query margin open orders"""

    client = Client(key, secret)
    response = client.margin_open_orders(**params)
    response.should.equal(mock_item)
