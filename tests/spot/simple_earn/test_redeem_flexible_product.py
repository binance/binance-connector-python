import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"productId": "product_001", "recvWindow": 5000}
expected_params = {"productId": "product_001", "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/simple-earn/flexible/redeem\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_redeem_flexible_product():
    """Tests the API endpoint to redeem flexible product"""

    client = Client(key, secret)
    response = client.redeem_flexible_product(**send_params)
    response.should.equal(mock_item)
