import pytest

from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

complete_params = {
    "algo": "sha256",
    "userName": "test",
    "startDate": 1617659086000,
    "endDate": 1607659086000,
    "toPoolUser": "S19pro",
    "hashRate": 100000000,
}

parameterized_test_data = [
    (
        {
            "algo": None,
            "userName": None,
            "startDate": None,
            "endDate": None,
            "toPoolUser": None,
            "hashRate": None,
        }
    ),
    (
        {
            "algo": "",
            "userName": "",
            "startDate": "",
            "endDate": "",
            "toPoolUser": "",
            "hashRate": "",
        }
    ),
    (
        {
            "algo": "sha256",
            "userName": "",
            "startDate": 1617659086000,
            "endDate": 1607659086000,
            "toPoolUser": "S19pro",
            "hashRate": 100000000,
        }
    ),
    (
        {
            "algo": "sha256",
            "userName": "test",
            "startDate": "",
            "endDate": 1607659086000,
            "toPoolUser": "S19pro",
            "hashRate": 100000000,
        }
    ),
    (
        {
            "algo": "sha256",
            "userName": "test",
            "startDate": 1617659086000,
            "endDate": "",
            "toPoolUser": "S19pro",
            "hashRate": 100000000,
        }
    ),
    (
        {
            "algo": "sha256",
            "userName": "test",
            "startDate": 1617659086000,
            "endDate": 1607659086000,
            "toPoolUser": "",
            "hashRate": 100000000,
        }
    ),
    (
        {
            "algo": "sha256",
            "userName": "test",
            "startDate": 1617659086000,
            "endDate": 1607659086000,
            "toPoolUser": "S19pro",
            "hashRate": "",
        }
    ),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_data)
async def test_mining_hashrate_resale_details_with_missing_field(params):
    """Tests the API endpoint to create a hashrate resale request with missing field"""
    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.mining_hashrate_resale_request(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/mining/hash-transfer/config\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
async def test_mining_hashrate_resale_request():
    """Tests the API endpoint to create a hashrate resale request"""

    client = Client(key, secret)
    response = await client.mining_hashrate_resale_request(**complete_params)
    response.should.equal(mock_item)
