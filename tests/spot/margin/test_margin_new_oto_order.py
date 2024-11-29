import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "symbol": "BNBUSDT",
    "workingType": "LIMIT",
    "workingSide": "SELL",
    "workingPrice": 600.0,
    "workingQuantity": 1.0,
    "pendingType": "LIMIT",
    "pendingSide": "BUY",
    "pendingQuantity": 1.0,
    "workingTimeInForce": "GTC",
    "pendingPrice": 595.0,
    "pendingTimeInForce": "GTC",
    "workingIcebergQty": 0.1,
}
expected_params = {
    "symbol": "BNBUSDT",
    "workingType": "LIMIT",
    "workingSide": "SELL",
    "workingPrice": 600.0,
    "workingQuantity": 1.0,
    "pendingType": "LIMIT",
    "pendingSide": "BUY",
    "pendingQuantity": 1.0,
    "workingTimeInForce": "GTC",
    "pendingPrice": 595.0,
    "pendingTimeInForce": "GTC",
    "workingIcebergQty": 0.1,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/order/oto\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_margin_new_oto_order():
    """Tests the API endpoint to post a new margin oto order"""

    client = Client(key, secret)
    response = client.margin_new_oto_order(**send_params)
    response.should.equal(mock_item)
