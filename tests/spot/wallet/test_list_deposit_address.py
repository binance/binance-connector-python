import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"coin": "BNB", "network": "BSC"}
expected_params = {"coin": "BNB", "network": "BSC"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/capital/deposit/address/list\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_list_deposit_address():
    """Tests the API endpoint to fetch deposit address list with network"""

    client = Client(key, secret)
    response = client.list_deposit_address(**send_params)
    response.should.equal(mock_item)
