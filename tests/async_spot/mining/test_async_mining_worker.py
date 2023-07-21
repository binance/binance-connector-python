import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_mining_worker_without_algo():
    """Tests the API endpoint to get worker without algo"""

    client = Client(key, secret)
    try:
        response = await client.mining_worker("", "test_name", "worker_name")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_mining_worker_without_username():
    """Tests the API endpoint to get worker without username"""

    client = Client(key, secret)
    try:
        response = await client.mining_worker("sha256", "", "worker_name")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_mining_worker_without_workername():
    """Tests the API endpoint to get worker without workername"""

    client = Client(key, secret)
    try:
        response = await client.mining_worker("sha256", "test_name", "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/mining/worker/detail\\?algo=sha256&userName=user_name&workerName=worker_name",
    mock_item,
    200,
)
async def test_mining_worker():
    """Tests the API endpoint to get coin list"""

    client = Client(key, secret)
    response = await client.mining_worker("sha256", "user_name", "worker_name")
    response.should.equal(mock_item)
