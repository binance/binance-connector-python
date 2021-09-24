import responses
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "quantity": 0.002,
    "price": 9500,
    "stopPrice": 7500,
    "stopLimitPrice": 7000,
    "stopLimitTimeInForce": "GTC",
    "recvWindow": 1000,
}


@mock_http_response(responses.POST, "/sapi/v1/margin/order/oco", mock_exception, 400)
def test_post_an_margin_oco_order_without_params():
    """Tests the API endpoint to post a new margin oco order without parameters"""

    client = Client(key, secret)
    client.new_margin_oco_order.when.called_with("", "", "", "", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/margin/order/oco\\?" + urlencode(params), mock_item, 200
)
def test_post_an_margin_oco_order():
    """Tests the API endpoint to post a new margin oco order"""

    client = Client(key, secret)
    response = client.new_margin_oco_order(**params)
    response.should.equal(mock_item)
