import responses

from urllib.parse import urlencode
from tests.util import timestamp
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "symbol": "ETHBTC",
    "orderId": "1234567",
    "origClientOrderId": "234567",
    "startTime": timestamp(),
    "endTime": timestamp(),
}


def test_get_orders_without_symbol():
    """Tests the API endpoint to get all orders without symbol"""

    client = Client(key, secret)
    client.get_orders.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/api/v3/allOrders\\?symbol=ETHBTC", mock_item, 200)
def test_get_orders():
    """Tests the API endpoint to get orders"""

    client = Client(key, secret)
    response = client.get_orders("ETHBTC")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/allOrders\\?" + urlencode(params), mock_item, 200
)
def test_get_orders_with_available_params():
    """Tests the API endpoint to get orders based on parameters"""

    client = Client(key, secret)
    response = client.get_orders(**params)
    response.should.equal(mock_item)
