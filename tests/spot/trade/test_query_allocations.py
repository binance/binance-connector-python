import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import current_timestamp
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "symbol": "BTCUSDT",
    "startTime": current_timestamp(),
    "endTime": current_timestamp(),
    "recvWindow": 5000,
}
expected_params = {
    "symbol": "BTCUSDT",
    "startTime": current_timestamp(),
    "endTime": current_timestamp(),
    "recvWindow": 5000,
}


@mock_http_response(
    responses.GET,
    "/api/v3/myAllocations\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_allocations():
    """Tests the API endpoint to get allocations resulting from SOR order placement"""

    client = Client(key, secret)
    response = client.query_allocations(**send_params)
    response.should.equal(mock_item)
