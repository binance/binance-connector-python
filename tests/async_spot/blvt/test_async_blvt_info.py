import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/blvt/tokenInfo", mock_item, 200)
async def test_blvt_info():
    """Tests the API endpoint to get BLVT Info"""

    client = Client(key, secret)
    response = await client.blvt_info()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/blvt/tokenInfo\\?tokenName=LINKUP", mock_item, 200
)
async def test_blvt_info_with_tokenName():
    """Tests the API endpoint to get BLVT Info with tokenName"""

    client = Client(key, secret)
    response = await client.blvt_info("LINKUP")
    response.should.equal(mock_item)
