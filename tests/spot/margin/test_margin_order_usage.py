import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"isIsolated": "TRUE", "symbol": "BNBUSDT"}

client = Client(key, secret)


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/rateLimit/order\\?" + urlencode(params),
    mock_item,
    200,
)
def test_margin_fee():
    """Tests the API endpoint to displays the user's current margin order count usage for all intervals"""

    response = client.margin_order_usage(**params)
    response.should.equal(mock_item)
