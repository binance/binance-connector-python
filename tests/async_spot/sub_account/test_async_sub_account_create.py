import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import urlencode as encoded_string

mock_item = {"key_1": "value_1"}

key = random_str()
secret = random_str()

params = {"subAccountString": "virtual.account", "recvWindow": 1000}

@pytest.mark.asyncio
async def test_sub_account_create_without_sub_account_string():
    """Tests the API endpoint to create sub-account without subAccountString"""

    client = Client(key, secret)
    try:
        response = await client.sub_account_create("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/sub-account/virtualSubAccount\\?" + encoded_string(params, True),
    mock_item,
    200,
)
async def test_sub_account_create():
    """Tests the API endpoint to create sub-account"""

    client = Client(key, secret)
    response = await client.sub_account_create(**params)
    response.should.equal(mock_item)
