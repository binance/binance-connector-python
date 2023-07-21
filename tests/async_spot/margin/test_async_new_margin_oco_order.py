import pytest
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "quantity": 0.002,
    "price": 9500,
    "stopPrice": 7500,
    "stopLimitPrice": 7000,
    "stopLimitTimeInForce": "GTC",
    "recvWindow": 1000,
}


@pytest.mark.asyncio
async def test_post_an_margin_oco_order_without_params():
    """Tests the API endpoint to post a new margin oco order without parameters"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.new_margin_oco_order("", "", "", "", "")


@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/margin/order/oco\\?" + urlencode(params), mock_item, 200
)
async def test_post_an_margin_oco_order():
    """Tests the API endpoint to post a new margin oco order"""

    client = Client(key, secret)
    response = await client.new_margin_oco_order(**params)
    response.should.equal(mock_item)
