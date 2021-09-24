import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ParameterArgumentError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "isIsolated": "TRUE",
    "symbol": "BNBUSDT",
    "fromId": "1234567",
    "limit": 10,
    "recvWindow": 1000,
}

client = Client(key, secret)


def test_get_margin_oco_orders_with_isIsolated_but_no_symbol():
    """Tests the API endpoint to get margin oco orders without symbol when having isIsolated"""

    client.get_margin_oco_orders.when.called_with(isIsolated="TRUE").should.throw(
        ParameterRequiredError
    )


def test_get_margin_oco_orders_with_fromId_and_startTime():
    """Tests the API endpoint to get margin oco orders with fromId and startTime"""

    client.get_margin_oco_orders.when.called_with(
        fromId=123456, startTime=1565245913407
    ).should.throw(ParameterArgumentError)


def test_get_margin_oco_orders_with_fromId_and_endTime():
    """Tests the API endpoint to get margin oco orders with fromId and endTime"""

    client.get_margin_oco_orders.when.called_with(
        fromId=123456, endTime=1565245913407
    ).should.throw(ParameterArgumentError)


@mock_http_response(responses.GET, "/sapi/v1/margin/allOrderList", mock_item, 200)
def test_get_margin_oco_orders_without_parameters():
    """Tests the API endpoint to get margin oco orders without parameters"""

    response = client.get_margin_oco_orders()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/allOrderList\\?" + urlencode(params), mock_item, 200
)
def test_get_margin_oco_orders_with_parameters():
    """Tests the API endpoint to get margin oco orders with parameters"""

    response = client.get_margin_oco_orders(**params)
    response.should.equal(mock_item)
