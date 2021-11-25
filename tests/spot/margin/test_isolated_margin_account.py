import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/isolated/account\\?" + urlencode({"symbols": "BTCUSDT,BNBUSDT"}),
    mock_item,
    200,
)
def test_isolated_margin_account():
    """Tests the API endpoint to get isolated margin account info"""

    client = Client(key, secret)
    response = client.isolated_margin_account(symbols="BTCUSDT,BNBUSDT")
    response.should.equal(mock_item)
