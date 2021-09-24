import responses
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

client = Client(key, secret)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/isolated/accountLimit", mock_item, 200
)
def test_enable_order_with_order_id():
    """Tests the API endpoint to query an isolated margin account limits"""

    response = client.isolated_margin_account_limit()
    response.should.equal(mock_item)
