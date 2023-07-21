import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "sapi/v1/bswap/poolConfigure", mock_item, 200)
async def test_bswap_pool_configure():
    """Tests the API endpoint to get pool configure"""

    client = Client(key, secret)
    response = await client.bswap_pool_configure()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "sapi/v1/bswap/poolConfigure\\?poolId=2", mock_item, 200
)
async def test_bswap_pool_configure_with_poolId():
    """Tests the API endpoint to get pool configure with poolId"""

    client = Client(key, secret)
    response = await client.bswap_pool_configure(poolId=2)
    response.should.equal(mock_item)
