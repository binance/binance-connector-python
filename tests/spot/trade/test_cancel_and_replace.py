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
    "side": "SELL",
    "type": "LIMIT",
    "cancelReplaceMode": "STOP_ON_FAILURE",
    "timeInForce": "GTC",
    "quantity": 10.1,
    "price": 295.92,
    "cancelOrderId": 12,
    "stopPrice": 20.01,
    "recvWindow": 5000,
}


@mock_http_response(responses.POST, "/api/v3/order", mock_exception, 400)
def test_cancel_and_replace_without_param():
    """Tests the API endpoint to post cancel an existing order and send a new order without parameters"""

    client = Client(key, secret)
    client.cancel_and_replace.when.called_with("", "", "", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/api/v3/order/cancelReplace\\?" + urlencode(params),
    mock_item,
    200,
)
def test_cancel_and_replace():
    """Tests the API endpoint to cancel an existing order and send a new order"""

    client = Client(key, secret)
    response = client.cancel_and_replace(**params)
    response.should.equal(mock_item)
