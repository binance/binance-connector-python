import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"vipLevel": 1, "symbol": "BNBUSDT"}

client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/margin/isolatedMarginData", mock_item, 200)
async def test_isolated_margin_fee_without_params():
    """Tests the API endpoint to get isolated margin fee data without params"""

    response = await client.isolated_margin_fee()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/isolatedMarginData\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_isolated_margin_fee():
    """Tests the API endpoint to get isolated margin fee data"""

    response = await client.isolated_margin_fee(**params)
    response.should.equal(mock_item)
