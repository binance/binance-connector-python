import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError
from binance.lib.utils import urlencode as encoded_string


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

email = "alice@test.com"
subAccountApiKey = random_str()
ipAddress = "1.2.3.4"

complete_params = {
    "email": email,
    "subAccountApiKey": subAccountApiKey,
    "ipAddress": ipAddress,
}

parameterized_test_params = [
    ({"email": None, "subAccountApiKey": None, "ipAddress": None}),
    ({"email": email, "subAccountApiKey": subAccountApiKey, "ipAddress": ""}),
    ({"email": email, "subAccountApiKey": "", "ipAddress": ipAddress}),
    ({"email": "", "subAccountApiKey": subAccountApiKey, "ipAddress": ipAddress}),
]

client = Client(key, secret)


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_params)
async def test_sub_account_api_delete_ip_with_missing_param(params):
    """Tests the API endpoint to delete IP for a sub-account API key with missing param"""

    with pytest.raises(ParameterRequiredError):
        await client.sub_account_api_delete_ip(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE",
    "/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList\\?"
    + encoded_string(complete_params, True),
    mock_item,
    200,
)
async def test_sub_account_api_delete_ip():
    """Tests the API endpoint to delete IP for a sub-account API key"""

    (await client.sub_account_api_delete_ip(**complete_params)).should.equal(mock_item)
