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

params = {"symbol": "BNBUSDT", "orderId": "orderId", "recvWindow": 1000}


@mock_http_response(responses.GET, "/sapi/v1/margin/order", mock_exception, 400)
def test_margin_order_without_symbol():
    """Tests the API endpoint to query margin order without symbol"""

    client = Client(key, secret)
    client.margin_order.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/order\\?" + urlencode(params), mock_item, 200
)
def test_margin_order():
    """Tests the API endpoint to query margin order"""

    client = Client(key, secret)
    response = client.margin_order(**params)
    response.should.equal(mock_item)
