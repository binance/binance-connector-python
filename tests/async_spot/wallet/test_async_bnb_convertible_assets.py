import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("POST", "/sapi/v1/asset/dust-btc", mock_item, 200)
async def test_bnb_convertible_assets():
    """Tests the API endpoint to get Assets That Can Be Converted Into BNB"""

    client = Client(key, secret)
    response = await client.bnb_convertible_assets()
    response.should.equal(mock_item)
