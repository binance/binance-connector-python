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
    "symbol": "BNBUSDT",
    "orderId": "order_id",
    "startTime": "1590969041003",
    "endTime": "1590969041003",
    "limit": 10,
    "recvWindow": 1000,
}


@mock_http_response(responses.GET, "/sapi/v1/margin/allOrders", mock_exception, 400)
def test_margin_all_orders_without_asset():
    """Tests the API endpoint to query margin all orders without symbol"""

    client = Client(key, secret)
    client.margin_all_orders.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/allOrders\\?" + urlencode(params), mock_item, 200
)
def test_margin_all_orders():
    """Tests the API endpoint to query margin all orders"""

    client = Client(key, secret)
    response = client.margin_all_orders(**params)
    response.should.equal(mock_item)
