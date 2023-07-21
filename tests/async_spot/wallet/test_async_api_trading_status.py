import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/account/apiTradingStatus", mock_item, 200)
async def test_api_trading_status():
    """Tests the API endpoint to check api trading status"""

    client = Client(key, secret)
    response = await client.api_trading_status()
    response.should.equal(mock_item)
