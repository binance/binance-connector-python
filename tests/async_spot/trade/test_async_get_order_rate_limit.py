import pytest
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/rateLimit/order", mock_item, 200)
async def test_get_order_rate_limit():
    """Tests the API endpoint to get current order count usage for all intervals."""
    response = await client.get_order_rate_limit()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/rateLimit/order\\?recvWindow=1000", mock_item, 200
)
async def test_get_order_rate_limit_with_recvWindow():
    """Tests the API endpoint to get current order count usage for all intervals."""
    response = await client.get_order_rate_limit(recvWindow=1000)
    response.should.equal(mock_item)
