import pytest

from urllib.parse import urlencode
from tests.util import timestamp
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
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

@pytest.mark.asyncio
async def test_get_orders_without_symbol():
    """Tests the API endpoint to get all orders without symbol"""

    client = Client(key, secret)
    try:
        response = await client.get_orders("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/allOrders\\?symbol=ETHBTC", mock_item, 200)
async def test_get_orders():
    """Tests the API endpoint to get orders"""

    client = Client(key, secret)
    response = await client.get_orders("ETHBTC")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/allOrders\\?" + urlencode(params), mock_item, 200
)
async def test_get_orders_with_available_params():
    """Tests the API endpoint to get orders based on parameters"""

    client = Client(key, secret)
    response = await client.get_orders(**params)
    response.should.equal(mock_item)
