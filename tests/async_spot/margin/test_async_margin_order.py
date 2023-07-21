import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"symbol": "BNBUSDT", "orderId": "orderId", "recvWindow": 1000}


@pytest.mark.asyncio
async def test_margin_order_without_symbol():
    """Tests the API endpoint to query margin order without symbol"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.margin_order("")


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/margin/order\\?" + urlencode(params), mock_item, 200
)
async def test_margin_order():
    """Tests the API endpoint to query margin order"""

    client = Client(key, secret)
    response = await client.margin_order(**params)
    response.should.equal(mock_item)
