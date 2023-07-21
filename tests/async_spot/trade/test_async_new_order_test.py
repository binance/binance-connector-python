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
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 0.002,
    "price": 9500,
    "recvWindow": 1000,
}


@pytest.mark.asyncio
async def test_post_an_order_testing_without_param():
    """Tests the API endpoint to check if sending post a new order for test only without param"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.new_order_test("", "", "")
    

@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/api/v3/order/test\\?" + urlencode(params), mock_item, 200
)
async def test_post_an_order_testing():
    """Tests the API endpoint to check if sending post a new order for test only"""

    client = Client(key, secret)
    response = await client.new_order_test(**params)
    response.should.equal(mock_item)
