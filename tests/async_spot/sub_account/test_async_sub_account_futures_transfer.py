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
    "email": "alice@test.com",
    "asset": "BNB",
    "amount": 100,
    "type": 1,
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_sub_account_futures_transfer_without_email():
    """Tests the API endpoint to futures transfer for Sub-account without email"""

    params = {"email": "", "asset": "BNB", "amount": 100, "type": 1, "recvWindow": 1000}
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_futures_transfer_without_asset():
    """Tests the API endpoint to futures transfer for Sub-account without asset"""

    params = {
        "email": "alice@test.com",
        "asset": "",
        "amount": 100,
        "type": 1,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_futures_transfer_without_amount():
    """Tests the API endpoint to futures transfer for Sub-account without amount"""

    params = {
        "email": "alice@test.com",
        "asset": "BNB",
        "amount": "",
        "type": 1,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_futures_transfer_without_type():
    """Tests the API endpoint to futures transfer for Sub-account without type"""

    params = {
        "email": "alice@test.com",
        "asset": "BNB",
        "amount": 100,
        "type": "",
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/sub-account/futures/transfer\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_sub_account_futures_transfer():
    """Tests the API endpoint to futures transfer for Sub-account"""

    client = Client(key, secret)
    response = await client.sub_account_futures_transfer(**params)
    response.should.equal(mock_item)
