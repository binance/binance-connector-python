import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
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

@pytest.mark.asyncio
async def test_get_margin_oco_orders_with_isIsolated_but_no_symbol():
    """Tests the API endpoint to get margin oco orders without symbol when having isIsolated"""

    try:
        response = await client.get_margin_oco_orders(isIsolated="TRUE")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_get_margin_oco_orders_with_fromId_and_startTime():
    """Tests the API endpoint to get margin oco orders with fromId and startTime"""

    try:
        response = await client.get_margin_oco_orders(
        fromId=123456, startTime=1565245913407
    )
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)

@pytest.mark.asyncio
async def test_get_margin_oco_orders_with_fromId_and_endTime():
    """Tests the API endpoint to get margin oco orders with fromId and endTime"""

    try:
        response = await client.get_margin_oco_orders(
        fromId=123456, endTime=1565245913407
    )
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/margin/allOrderList", mock_item, 200)
async def test_get_margin_oco_orders_without_parameters():
    """Tests the API endpoint to get margin oco orders without parameters"""

    response = await client.get_margin_oco_orders()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/margin/allOrderList\\?" + urlencode(params), mock_item, 200
)
async def test_get_margin_oco_orders_with_parameters():
    """Tests the API endpoint to get margin oco orders with parameters"""

    response = await client.get_margin_oco_orders(**params)
    response.should.equal(mock_item)
