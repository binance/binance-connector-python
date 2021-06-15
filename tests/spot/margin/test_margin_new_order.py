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
    "quantity": 0.001,
    "timeInForce": "GTC",
    "price": 9500,
    "recvWindow": 1000,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/order\\?symbol=&side=SELL&type=LIMIT&quantity=0.001",
    mock_exception,
    400,
)
def test_post_an_margin_order_without_symbol():
    """Tests the API endpoint to post a new margin order without symbol"""

    client = Client(key, secret)
    client.new_margin_order.when.called_with(
        symbol="", side="SELL", type="LIMIT", quantity=0.02
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/order\\?symbol=BTCUSDT&side=&type=LIMIT&quantity=0.001",
    mock_exception,
    400,
)
def test_post_an_margin_order_without_side():
    """Tests the API endpoint to post a new margin order without side"""

    client = Client(key, secret)
    client.new_margin_order.when.called_with(
        symbol="BTCUSDT", side="", type="LIMIT", quantity=0.02
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/order\\?symbol=BTCUSDT&side=SELL&type=&quantity=0.001",
    mock_exception,
    400,
)
def test_post_an_margin_order_without_type():
    """Tests the API endpoint to post a new margin order without parameters"""

    client = Client(key, secret)
    client.new_margin_order.when.called_with(
        symbol="BTCUSDT", side="SELL", type="", quantity=0.02
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST, "/sapi/v1/margin/order\\?" + urlencode(params), mock_item, 200
)
def test_post_an_margin_order():
    """Tests the API endpoint to post a new margin order"""

    client = Client(key, secret)
    response = client.new_margin_order(**params)
    response.should.equal(mock_item)
