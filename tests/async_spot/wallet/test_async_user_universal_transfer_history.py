import pytest

from binance.error import ParameterRequiredError, ParameterValueError
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_user_universal_transfer_with_missing_field():
    """Tests the API endpoint to query universal transfer history with missing field"""

    client = Client(key, secret)
    try:
        response = await client.user_universal_transfer_history("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_user_universal_transfer_with_invalid_enum_string():
    """Tests the API endpoint to query universal transfer history with invalid string"""

    client = Client(key, secret)
    try:
        response = await client.user_universal_transfer_history(random_str())
    except Exception as e:
        assert isinstance(e, ParameterValueError)
    else:
        assert isinstance(response, ParameterValueError)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/asset/transfer\\?type=UMFUTURE_MAIN", mock_item, 200
)
async def test_user_universal_transfer():
    """Tests the API endpoint to query universal transfer history"""

    client = Client(key, secret)
    response = await client.user_universal_transfer_history("UMFUTURE_MAIN")
    response.should.equal(mock_item)
