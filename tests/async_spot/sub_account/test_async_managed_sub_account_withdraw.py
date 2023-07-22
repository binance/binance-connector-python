import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import urlencode as encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {
    "fromEmail": "alice@test.com",
    "asset": "BNB",
    "amount": 1,
    "transferDate": 1624023242,
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_managed_sub_account_withdraw_assets_without_fromEmail():
    """Tests the API endpoint to withdraw asset from managed sub account without toEmail"""

    params = {
        "fromEmail": "",
        "asset": "BNB",
        "amount": 1,
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_withdraw(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_managed_sub_account_withdraw_assets_without_asset():
    """Tests the API endpoint to withdraw asset from managed sub account without asset"""

    params = {
        "fromEmail": "alice@test.com",
        "asset": "",
        "amount": 1,
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_withdraw(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_managed_sub_account_withdraw_assets_without_amount():
    """Tests the API endpoint to withdraw asset from managed sub account without amount"""

    params = {
        "fromEmail": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "transferDate": 1624023242,
        "recvWindow": 1000,
    }

    client = Client(key, secret)
    try:
        response = await client.managed_sub_account_withdraw(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/managed-subaccount/withdraw\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_managed_sub_account_withdraw_assets():
    """Tests the API endpoint to withdraw asset from managed sub account"""

    client = Client(key, secret)
    response = await client.managed_sub_account_withdraw(**params)
    response.should.equal(mock_item)
