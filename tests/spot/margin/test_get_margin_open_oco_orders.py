import responses
from urllib.parse import urlencode
from binance.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "isIsolated": "TRUE",
    "symbol": "BNBUSDT",
}

client = Client(key, secret)


def test_get_margin_open_oco_orders_with_isIsolated_but_no_symbol():
    """Tests the API endpoint to get margin oco orders without symbol when having isIsolated"""
    client.get_margin_open_oco_orders.when.called_with(isIsolated="TRUE").should.throw(
        ParameterRequiredError
    )


@mock_http_response(responses.GET, "/sapi/v1/margin/openOrderList", mock_item, 200)
def test_get_margin_open_oco_orders_without_parameters():
    """Tests the API endpoint to get all margin open oco orders without parameters"""

    response = client.get_margin_open_oco_orders()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/openOrderList\\?" + urlencode(params),
    mock_item,
    200,
)
def test_get_margin_open_oco_orders_with_parameters():
    """Tests the API endpoint to get all margin open oco orders with parameters"""

    response = client.get_margin_open_oco_orders(**params)
    response.should.equal(mock_item)
