import responses
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

client = Client(key, secret)


@mock_http_response(responses.GET, "/api/v3/rateLimit/order", mock_item, 200)
def test_get_order_rate_limit():
    """Tests the API endpoint to get current order count usage for all intervals."""
    response = client.get_order_rate_limit()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/rateLimit/order\\?recvWindow=1000", mock_item, 200
)
def test_get_order_rate_limit_with_recvWindow():
    """Tests the API endpoint to get current order count usage for all intervals."""
    response = client.get_order_rate_limit(recvWindow=1000)
    response.should.equal(mock_item)
