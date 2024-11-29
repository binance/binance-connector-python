import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"amount": 1.0, "recvWindow": 5000}
expected_params = {"amount": 1.0, "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/eth-staking/wbeth/wrap\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_wrap_beth():
    """Tests the API endpoint to wrap BETH"""

    client = Client(key, secret)
    response = client.wrap_beth(**send_params)
    response.should.equal(mock_item)
