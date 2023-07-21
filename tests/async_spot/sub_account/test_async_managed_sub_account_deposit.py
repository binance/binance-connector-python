import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {"toEmail": "alice@test.com", "asset": "BNB", "amount": 1, "recvWindow": 1000}

@pytest.mark.asyncio
async def test_managed_sub_account_deposit_assets_without_toEmail():
    """Tests the API endpoint to transfer asset to managed sub account without toEmail"""

    params = {"toEmail": "", "asset": "BNB", "amount": 1, "recvWindow": 1000}
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_deposit(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_managed_sub_account_deposit_assets_without_asset():
    """Tests the API endpoint to transfer asset to managed sub account without asset"""

    params = {"toEmail": "alice@test.com", "asset": "", "amount": 1, "recvWindow": 1000}
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_deposit(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_managed_sub_account_deposit_assets_without_amount():
    """Tests the API endpoint to transfer asset to managed sub account without amount"""

    params = {
        "toEmail": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "recvWindow": 1000,
    }

    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_deposit(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/managed-subaccount/deposit\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_managed_sub_account_deposit_assets():
    """Tests the API endpoint to transfer asset to managed sub account"""

    client = Client(key, secret)
    response = await client.managed_sub_account_deposit(**params)
    response.should.equal(mock_item)
