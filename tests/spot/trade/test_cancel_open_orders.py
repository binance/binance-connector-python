import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -2011, "msg": "unknown order sent"}

key = random_str()
secret = random_str()

orderId = "1234567"
origClientOrderId = "2345678"

params = {"symbol": "ETHBTC", "recvWindow": 1000}


def test_cancel_open_orders_without_symbol():
    """Tests the API endpoint to cancel all open orders without symbol"""

    client = Client(key, secret)
    client.cancel_open_orders.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.DELETE, "/api/v3/openOrders\\?symbol=ETHBTC", mock_exception, 400
)
def test_cancel_open_orders_when_no_open_orders():
    """Tests the API endpoint to cancel all open orders when there is no open order"""

    client = Client(key, secret)
    client.cancel_open_orders.when.called_with("ETHBTC").should.throw(ClientError)


@mock_http_response(
    responses.DELETE, "/api/v3/openOrders\\?" + urlencode(params), mock_item, 200
)
def test_cancel_open_orders():
    """Tests the API endpoint to cancel all open orders"""

    client = Client(key, secret)
    response = client.cancel_open_orders("ETHBTC", recvWindow=1000)
    response.should.equal(mock_item)
