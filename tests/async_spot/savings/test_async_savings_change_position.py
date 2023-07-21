import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_change_fixed_activity_position_to_daily_position_without_projectId():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position without projectId"""

    client = Client(key, secret)
    try:
        response = await client.savings_change_position("", "1")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_change_fixed_activity_position_to_daily_position_without_lot():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position without lot"""

    client = Client(key, secret)
    try:
        response = await client.savings_change_position("USDT001", None)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/lending/positionChanged\\?projectId=USDT001&lot=1",
    mock_item,
    200,
)
async def test_change_fixed_activity_position_to_daily_position():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position"""

    client = Client(key, secret)
    response = await client.savings_change_position(projectId="USDT001", lot="1")
    response.should.equal(mock_item)
