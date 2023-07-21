import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/sub-account/status\\?email=alice@test.com", mock_item, 200
)
async def test_sub_account_asset():
    """Tests the API endpoint to  get sub account asset"""

    client = Client(key, secret)
    response = await client.sub_account_status(email="alice@test.com")
    response.should.equal(mock_item)
