import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

client = Client(key, secret)

@pytest.mark.asyncio
async def test_mining_account_earning_without_algo():
    """Tests the API endpoint to get account earnings without algo"""

    try:
        response = await client.mining_account_earning("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/mining/payment/uid\\?algo=sha256", mock_item, 200
)
async def test_mining_account_earning():
    """Tests the API endpoint to get account earnings"""

    (await client.mining_account_earning(algo="sha256")).should.equal(mock_item)
