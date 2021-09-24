import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "fromId": "1234567",  # If supplied, neither startTime or endTime can be provided
    "limit": 10,
    "recvWindow": 1000,
}


@mock_http_response(responses.GET, "/api/v3/allOrderList", mock_item, 200)
def test_get_oco_orders_without_parameters():
    """Tests the API endpoint to get oco orders without parameters"""

    client = Client(key, secret)
    response = client.get_oco_orders()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/allOrderList\\?" + urlencode(params), mock_item, 200
)
def test_get_oco_orders_with_parameters():
    """Tests the API endpoint to get oco orders with provided parameters"""

    client = Client(key, secret)
    response = client.get_oco_orders(**params)
    response.should.equal(mock_item)
