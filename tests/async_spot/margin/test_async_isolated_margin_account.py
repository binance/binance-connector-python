import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/isolated/account\\?" + urlencode({"symbols": "BTCUSDT,BNBUSDT"}),
    mock_item,
    200,
)
async def test_isolated_margin_account():
    """Tests the API endpoint to get isolated margin account info"""

    client = Client(key, secret)
    response = await client.isolated_margin_account(symbols="BTCUSDT,BNBUSDT")
    response.should.equal(mock_item)
