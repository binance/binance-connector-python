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
    "coin": "BNB",
    "status": 1,
    "startTime": "1591142602820",
    "endTime": "1591142602820",
    "limit": 100,
    "offset": 10,
    "recvWindow": 1000,
}

@pytest.mark.asyncio
async def test_sub_account_deposit_history_without_email():
    """Tests the API endpoint to get deposit history without email"""

    params = {
        "email": "",
        "coin": "BNB",
        "status": 1,
        "startTime": "1591142602820",
        "endTime": "1591142602820",
        "limit": 100,
        "offset": 10,
        "recvWindow": 1000,
    }
    client = Client(key, secret)
    try:
        response = await client.sub_account_deposit_history(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/capital/deposit/subHisrec\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_sub_account_deposit_address():
    """Tests the API endpoint to get deposit history"""

    client = Client(key, secret)
    response = await client.sub_account_deposit_history(**params)
    response.should.equal(mock_item)
