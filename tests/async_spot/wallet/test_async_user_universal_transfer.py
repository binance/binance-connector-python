import pytest

from binance.error import ParameterRequiredError, ParameterValueError
from binance.lib.utils import encoded_string
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

complete_params = {"type": "UMFUTURE_MAIN", "asset": "BNB", "amount": 0.1}

parameterized_test_params = [
    ({"type": None, "asset": None, "amount": None}),
    ({"type": "", "asset": "BNB", "amount": 0.1}),
    ({"type": "UMFUTURE_MAIN", "asset": "", "amount": 0.1}),
    ({"type": "UMFUTURE_MAIN", "asset": "BNB", "amount": ""}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_params)
async def test_user_universal_transfer_with_missing_field(params):
    """Tests the API endpoint to transfer from one account to another with missing field"""

    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.user_universal_transfer(**params)


@pytest.mark.asyncio
async def test_user_universal_transfer_with_invalid_enum_string():
    """Tests the API endpoint to transfer from one account to another with invalid string"""

    invalid_params = {"type": random_str(), "asset": "BNB", "amount": 0.1}
    client = Client(key, secret)
    with pytest.raises(ParameterValueError):
        await client.user_universal_transfer(**invalid_params)

@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/asset/transfer\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
async def test_user_universal_transfer():
    """Tests the API endpoint to transfer from one account to another"""

    client = Client(key, secret)
    response = await client.user_universal_transfer(**complete_params)
    response.should.equal(mock_item)
