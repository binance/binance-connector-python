import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from urllib.parse import urlencode
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

params = {
    "coin": "BNB",
    "amount": 1,
    "address": random_str(),
    "withdrawOrderId": "1234567",
    "network": "BNB",
    "addressTag": random_str(),
    "transactionFeeFlag": "true",
    "name": "test_address",
    "walletType": 0,
}

@pytest.mark.asyncio
async def test_withdraw_without_coin():
    """Tests the API endpoint to withdraw without coin"""

    client = Client(key, secret)
    try:
        response = await client.withdraw("", 1, "address")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_withdraw_without_amount():
    """Tests the API endpoint to withdraw without amount"""

    client = Client(key, secret)
    try:
        response = await client.withdraw("BNB", "", "address")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_withdraw_without_address():
    """Tests the API endpoint to withdraw without address"""

    client = Client(key, secret)
    try:
        response = await client.withdraw("BNB", 1, "")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/capital/withdraw/apply\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_withdraw():
    """Tests the API endpoint to withdraw"""

    client = Client(key, secret)
    response = await client.withdraw(**params)
    response.should.equal(mock_item)
