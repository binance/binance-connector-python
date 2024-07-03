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
    "symbol": "BNBUSDT",
    "workingType": "LIMIT",
    "workingSide": "BUY",
    "workingPrice": 400,
    "workingQuantity": 1,
    "pendingSide": "BUY",
    "pendingQuantity": 1,
    "pendingAboveType": "LIMIT_MAKER",
    "workingTimeInForce": "GTC",
    "pendingPrice": 400,
    "pendingTimeInForce": "GTC",
}


@mock_http_response(responses.POST, "/api/v3/order/otoco", mock_exception, 400)
def test_post_an_otoco_order_without_param():
    """Tests the API endpoint to post a new otoco order without parameters"""

    client = Client(key, secret)
    client.new_otoco_order.when.called_with(
        "", "", "", "", "", "", "", ""
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST, "/api/v3/orderList/otoco\\?" + urlencode(params), mock_item, 200
)
def test_post_an_otoco_order():
    """Tests the API endpoint to post a new otoco order"""

    client = Client(key, secret)
    response = client.new_otoco_order(**params)
    response.should.equal(mock_item)
