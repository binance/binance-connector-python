import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_mining_statistics_list_without_algo():
    """Tests the API endpoint to get statistics list without algo"""

    client = Client(key, secret)
    try:
        response = await client.mining_statistics_list("", "test_name")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_mining_statistics_list_without_username():
    """Tests the API endpoint to get statistics list without username"""

    client = Client(key, secret)
    try:
        response = await client.mining_statistics_list("sha256", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/mining/statistics/user/status\\?algo=sha256&userName=user_name",
    mock_item,
    200,
)
async def test_mining_statistics():
    """Tests the API endpoint to get statistics list"""

    client = Client(key, secret)
    response = await client.mining_statistics_list("sha256", "user_name")
    response.should.equal(mock_item)
