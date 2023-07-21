import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_savings_flexible_user_left_quota_without_productId():
    """Tests the API endpoint to get left daily purchase quota of flexible product without productId"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_user_left_quota("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/lending/daily/userLeftQuota\\?productId=1", mock_item, 200
)
async def test_savings_flexible_user_left_quota():
    """Tests the API endpoint to get left daily purchase quota of flexible product"""

    client = Client(key, secret)
    response = await client.savings_flexible_user_left_quota(productId=1)
    response.should.equal(mock_item)
