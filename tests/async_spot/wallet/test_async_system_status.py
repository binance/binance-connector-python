import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/system/status", mock_item, 200)
async def test_system_status():
    """Tests the API endpoint to check system status"""

    client = Client(key, secret)
    response = await client.system_status()
    response.should.equal(mock_item)
