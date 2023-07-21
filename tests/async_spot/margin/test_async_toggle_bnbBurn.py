import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("POST", "/sapi/v1/bnbBurn", mock_item, 200)
async def test_toggle_bnbBurn():
    """Tests the API endpoint to Toggle BNBBurn On Spot Trade And Margin Interest"""

    client = Client(key, secret)
    response = await client.toggle_bnbBurn()
    response.should.equal(mock_item)
