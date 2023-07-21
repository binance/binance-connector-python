import pytest

from binance.lib.utils import encoded_string
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "email": "alice@test.com",
    "futuresType": 1,  # 1:USDT Margined Futures, 2:COIN Margined Futures
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_sub_account_futures_account_v2_without_email():
    """Tests the API endpoint to get sub account futures account without email"""

    params = {"email": "", "futuresType": 1, "recvWindow": 1000}

    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_account(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_sub_account_futures_account_v2_without_futuresType():
    """Tests the API endpoint to get sub account futures account without futuresType"""

    params = {"email": "alice@test.com", "futuresType": "", "recvWindow": 1000}

    client = Client(key, secret)
    try:
        response = await client.sub_account_futures_account(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v2/sub-account/futures/account\\?" + encoded_string(params),
    mock_item,
    200,
)
async def test_sub_account_futures_account_v2():
    """Tests the API endpoint to get sub account futures account"""

    client = Client(key, secret)
    response = await client.sub_account_futures_account(**params)
    response.should.equal(mock_item)
