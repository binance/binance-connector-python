import pytest
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BTCUSDT",
    "recvWindow": 1000,
}

client = Client(key, secret)

@pytest.mark.asyncio
async def test_enable_isolated_margin_account_without_symbol():
    """Tests the API endpoint to enable an isolated margin account without symbol"""

    try:
        response = await client.enable_isolated_margin_account("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/margin/isolated/account\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_enable_isolated_margin_account():
    """Tests the API endpoint to enable an isolated margin account"""

    response = await client.enable_isolated_margin_account(**params)
    response.should.equal(mock_item)
