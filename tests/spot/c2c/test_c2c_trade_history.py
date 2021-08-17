import responses

from tests.util import random_str, timestamp
from tests.util import mock_http_response
from urllib.parse import urlencode
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "tradeType": "BUY",
    "startTimestamp": timestamp(),
    "endTimestamp": timestamp(),
    "page": 1,
    "rows": 100,
}


def test_c2c_trade_history_without_trade_type():
    """Tests the API endpoint of c2c trade history without trade type"""
    client = Client(key, secret)
    client.c2c_trade_history.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET,
    "/sapi/v1/c2c/orderMatch/listUserOrderHistory\\?" + urlencode(params),
    mock_item,
    200,
)
def test_c2c_trade_history():
    """Tests the API endpoint to get c2c trade history"""

    client = Client(key, secret)
    response = client.c2c_trade_history(**params)
    response.should.equal(mock_item)
