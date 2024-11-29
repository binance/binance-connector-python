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
    "workingSide": "BUY",
    "workingPrice": 600.0,
    "workingQuantity": 1.0,
    "pendingSide": "SELL",
    "pendingQuantity": 1.0,
    "pendingAboveType": "LIMIT_MAKER",
    "workingTimeInForce": "GTC",
    "pendingAbovePrice": 605.0,
    "pendingBelowType": "LIMIT_MAKER",
    "pendingBelowPrice": 595.0,
    "workingIcebergQty": 0.1,
}
expected_params = {
    "symbol": "BNBUSDT",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingPrice": 600.0,
    "workingQuantity": 1.0,
    "pendingSide": "SELL",
    "pendingQuantity": 1.0,
    "pendingAboveType": "LIMIT_MAKER",
    "workingTimeInForce": "GTC",
    "pendingAbovePrice": 605.0,
    "pendingBelowType": "LIMIT_MAKER",
    "pendingBelowPrice": 595.0,
    "workingIcebergQty": 0.1,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/order/otoco\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_margin_new_otoco_order():
    """Tests the API endpoint to post a new margin otoco order"""

    client = Client(key, secret)
    response = client.margin_new_otoco_order(**send_params)
    response.should.equal(mock_item)
