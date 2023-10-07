import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"maxLeverage": 3, "recvWindow": 5000}
expected_params = {"maxLeverage": 3, "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/max-leverage\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_adjust_cross_margin_max_leverage():
    """Tests the API endpoint to adjust cross margin max leverage"""

    client = Client(key, secret)
    response = client.adjust_cross_margin_max_leverage(**send_params)
    response.should.equal(mock_item)
