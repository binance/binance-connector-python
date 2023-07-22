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

complete_params = {
    "email": email,
    "subAccountApiKey": subAccountApiKey,
    "status": "1",
}

parameterized_test_params = [
    ({"email": None, "subAccountApiKey": None, "status": None}),
    ({"email": email, "subAccountApiKey": subAccountApiKey, "status": ""}),
    ({"email": email, "subAccountApiKey": "", "status": "1"}),
    ({"email": "", "subAccountApiKey": subAccountApiKey, "status": "1"}),
]

client = Client(key, secret)


@pytest.mark.asyncio
@pytest.mark.parametrize("params", parameterized_test_params)
async def test_sub_account_update_ip_restriction_with_missing_param(params):
    """Tests the API endpoint to update IP restriction for a sub-account API key with missing param"""

    with pytest.raises(ParameterRequiredError):
        await client.sub_account_update_ip_restriction(**params)


@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v2/sub-account/subAccountApi/ipRestriction\\?"
    + encoded_string(complete_params, True),
    mock_item,
    200,
)
async def test_sub_account_update_ip_restriction():
    """Tests the API endpoint to update IP restriction for a sub-account API key"""

    (await client.sub_account_update_ip_restriction(**complete_params)).should.equal(mock_item)
