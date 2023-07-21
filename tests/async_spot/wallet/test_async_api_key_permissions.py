import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/sapi/v1/account/apiRestrictions", mock_item, 200)
async def test_funding_wallet():
    """Tests the API endpoint to obtain the api key's permissions"""

    client = Client(key, secret)
    response = await client.api_key_permissions()
    response.should.equal(mock_item)
