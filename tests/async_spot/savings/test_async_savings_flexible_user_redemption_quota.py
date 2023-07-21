import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_savings_flexible_user_redemption_quota_without_productId():
    """Tests the API endpoint to get left daily redemption quota of flexible Product without productId"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_user_redemption_quota("", 10)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_savings_flexible_user_redemption_quota_without_type():
    """Tests the API endpoint to get left daily redemption quota of flexible Product without type"""

    client = Client(key, secret)
    try:
        response = await client.savings_flexible_user_redemption_quota(
        "1", None
    )
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/lending/daily/userRedemptionQuota\\?productId=1&type=2",
    mock_item,
    200,
)
async def test_savings_flexible_user_redemption_quota():
    """Tests the API endpoint to get left daily redemption quota of flexible Product"""

    client = Client(key, secret)
    response = await client.savings_flexible_user_redemption_quota(productId=1, type=2)
    response.should.equal(mock_item)
