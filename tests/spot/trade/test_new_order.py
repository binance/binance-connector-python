import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 0.002,
    "price": 9500,
    "recvWindow": 1000,
}


@mock_http_response(responses.POST, "/api/v3/order", mock_exception, 400)
def test_post_an_order_without_param():
    """Tests the API endpoint to post a new order without parameters"""

    client = Client(key, secret)
    client.new_order.when.called_with("", "", "").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST, "/api/v3/order\\?" + urlencode(params), mock_item, 200
)
def test_post_an_order():
    """Tests the API endpoint to post a new order"""

    client = Client(key, secret)
    response = client.new_order(**params)
    response.should.equal(mock_item)
