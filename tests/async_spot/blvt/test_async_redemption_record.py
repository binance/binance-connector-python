import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/blvt/redeem/record", mock_item, 200)
async def test_redemption_record():
    """Tests the API endpoint to Query Redemption Record"""

    client = Client(key, secret)
    response = await client.redemption_record()
    response.should.equal(mock_item)
