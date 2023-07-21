import pytest

from binance.error import ParameterRequiredError
from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"symbol": "BNBUSDT", "recvWindow": 1000}

@pytest.mark.asyncio
async def test_margin_open_orders_cancellation_without_symbol():
    """Tests the API endpoint to cancel margin open orders without symbol"""

    client = Client(key, secret)
    try:
        response = await client.margin_open_orders_cancellation("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE",
    "/sapi/v1/margin/openOrders\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_margin_open_orders_cancellation():
    """Tests the API endpoint to cancel margin open orders"""

    client = Client(key, secret)
    response = await client.margin_open_orders_cancellation(**params)
    response.should.equal(mock_item)
