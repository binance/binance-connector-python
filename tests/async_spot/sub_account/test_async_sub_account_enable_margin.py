import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import urlencode as encode_string


mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_sub_account_enable_margin_without_email():
    """Tests the API endpoint to enable margin without email"""

    client = Client(key, secret)
    try:
        response = await client.sub_account_enable_margin("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/sub-account/margin/enable\\?"+encode_string({"email":"alice@test.com"}, True),
    mock_item,
    200,
)
async def test_sub_account_enable_margin():
    """Tests the API endpoint to enable margin"""

    client = Client(key, secret)
    response = await client.sub_account_enable_margin(email="alice@test.com")
    response.should.equal(mock_item)
