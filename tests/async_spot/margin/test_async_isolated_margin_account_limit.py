import pytest
from tests.util import random_str
from tests.util import mock_async_http_response
from urllib.parse import urlencode
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

client = Client(key, secret)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/isolated/accountLimit\\?" + urlencode({"recvWindow": 6000}),
    mock_item,
    200,
)
async def test_isolated_margin_account_limit_with_recvWindow():
    """Tests the API endpoint to query an isolated margin account limits"""

    response = await client.isolated_margin_account_limit(recvWindow=6000)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/margin/isolated/accountLimit", mock_item, 200
)
async def test_isolated_margin_account_limit():
    """Tests the API endpoint to query an isolated margin account limits"""

    response = await client.isolated_margin_account_limit()
    response.should.equal(mock_item)
