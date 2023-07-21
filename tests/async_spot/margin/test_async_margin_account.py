import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/margin/account", mock_item, 200)
async def test_margin_account():
    """Tests the API endpoint to margin account information"""

    client = Client(key, secret)
    response = await client.margin_account()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/margin/account\\?recvWindow=10000", mock_item, 200
)
async def test_margin_account_with_recvWindow():
    """Tests the API endpoint to margin account information with recvWindow"""

    client = Client(key, secret)
    response = await client.margin_account(recvWindow=10000)
    response.should.equal(mock_item)
