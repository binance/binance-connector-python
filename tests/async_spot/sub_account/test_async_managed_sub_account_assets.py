import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {"email": "alice@test.com", "recvWindow": 1000}

@pytest.mark.asyncio
async def test_managed_sub_account_query_assets_without_email():
    """Tests the API endpoint to query asset from managed sub account without email"""

    params = {"email": "", "recvWindow": 1000}
    client = Client(key, secret)
    with pytest.raises(ParameterRequiredError):
        await client.managed_sub_account_assets(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/managed-subaccount/asset\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_managed_sub_account_withdraw_assets():
    """Tests the API endpoint to query asset from managed sub account"""

    client = Client(key, secret)
    response = await client.managed_sub_account_assets(**params)
    response.should.equal(mock_item)
