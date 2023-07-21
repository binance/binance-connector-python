import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"email": "alice@test.com", "type": "SPOT"}

@pytest.mark.asyncio
async def test_managed_sub_account_get_snapshot_without_email():
    """Tests the API endpoint to query managed sub-account snapshot without email"""

    params = {"email": "", "type": "SPOT"}
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_get_snapshot(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_managed_sub_account_get_snapshot_without_type():
    """Tests the API endpoint to query managed sub-account snapshot without type"""

    params = {"email": "alice@test.com", "type": ""}
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_get_snapshot(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/managed-subaccount/accountSnapshot\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_managed_sub_account_get_snapshot():
    """Tests the API endpoint to query managed sub-account snapshot"""

    client = Client(key, secret)
    response = await client.managed_sub_account_get_snapshot(**params)
    response.should.equal(mock_item)
