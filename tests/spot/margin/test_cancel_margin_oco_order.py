import responses
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "orderListId": 1,
    "listClientOrderId": 2,
    "newClientOrderId": 3,
    "recvWindow": 1000,
}

client = Client(key, secret)


def test_cancel_margin_oco_order_without_symbol():
    """Tests the API endpoint to cancel margin oco order without symbol"""

    client.cancel_margin_oco_order.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.DELETE, "/sapi/v1/margin/orderList\\?" + urlencode(params), mock_item, 200
)
def test_cancel_margin_oco_order():
    """Tests the API endpoint to cancel oco order"""

    response = client.cancel_margin_oco_order(**params)
    response.should.equal(mock_item)
