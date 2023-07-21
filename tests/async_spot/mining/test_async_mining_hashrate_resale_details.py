import pytest

from binance.error import ParameterRequiredError
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

parameterized_test_data = [
    ({"configId": None, "userName": None}),
    ({"configId": "", "userName": "user_name"}),
    ({"configId": 123, "userName": ""}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_data)
async def test_mining_hashrate_resale_details_with_missing_field(params):
    """Tests the API endpoint to get hashrate resale details with missing field"""
    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.mining_hashrate_resale_details(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/mining/hash-transfer/profit/details\\?configId=123&userName=user_name",
    mock_item,
    200,
)
async def test_mining_hashrate_resale_details():
    """Tests the API endpoint to get hashrate resale details"""

    client = Client(key, secret)
    response = await client.mining_hashrate_resale_details(123, "user_name")
    response.should.equal(mock_item)
