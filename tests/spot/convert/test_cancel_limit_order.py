import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"orderId": 1603680255057330400, "recvWindow": 5000}
expected_params = {"orderId": 1603680255057330400, "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/convert/limit/cancelOrder\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_cancel_limit_order():
    """Tests the API endpoint to cancel a limit order"""

    client = Client(key, secret)
    response = client.cancel_limit_order(**send_params)
    response.should.equal(mock_item)
