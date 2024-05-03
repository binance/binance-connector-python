import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"type": "MARGIN", "recvWindow": 5000}
expected_params = {"type": "MARGIN", "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/available-inventory\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_margin_available_inventory():
    """Tests the API endpoint to margin available inventory"""

    client = Client(key, secret)
    response = client.margin_available_inventory(**send_params)
    response.should.equal(mock_item)
