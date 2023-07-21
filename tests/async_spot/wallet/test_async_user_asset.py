import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {"asset": "BNB", "recvWindow": 5000}


@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v3/asset/getUserAsset\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_user_asset():
    """Tests the API endpoint to user asset"""

    client = Client(key, secret)
    response = await client.user_asset(**params)
    response.should.equal(mock_item)
