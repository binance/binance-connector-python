import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"symbol": "BNBUSDT", "tier": 1}

client = Client(key, secret)


@pytest.mark.asyncio
async def test_isolated_margin_tier_without_symbol():
    """Tests the API endpoint to get isolated margin tier data without params"""

    with pytest.raises(ParameterRequiredError):
        await client.isolated_margin_tier("")


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/isolatedMarginTier\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_isolated_margin_tier():
    """Tests the API endpoint to get isolated margin tier data"""

    response = await client.isolated_margin_tier(**params)
    response.should.equal(mock_item)
