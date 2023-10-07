import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"recvWindow": 5000}
expected_params = {"recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/dust\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_get_assets_that_can_be_converted_into_bnb():
    """Tests the API endpoint to get assets that can be converted into bnb"""

    client = Client(key, secret)
    response = client.get_assets_that_can_be_converted_into_bnb(**send_params)
    response.should.equal(mock_item)
