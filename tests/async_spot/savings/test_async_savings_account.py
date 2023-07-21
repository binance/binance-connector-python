import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/lending/union/account", mock_item, 200)
async def test_savings_account():
    """Tests the API endpoint to get lending account"""

    client = Client(key, secret)
    response = await client.savings_account()
    response.should.equal(mock_item)
