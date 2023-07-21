import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_new_isolated_margin_listen_key_without_symbol():
    """Tests the API endpoint to create a new isolated margin listen key without symbol"""

    client = Client(key, secret)
    try:
        response = await client.new_isolated_margin_listen_key("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST", "/sapi/v1/userDataStream/isolated\\?symbol=BTCUSDT", mock_item, 200
)
async def test_new_isolated_margin_listen_key():
    """Tests the API endpoint to create a new isolated margin listen key"""

    param = {"symbol": "BTCUSDT"}
    client = Client(key)
    response = await client.new_isolated_margin_listen_key(**param)
    response.should.equal(mock_item)
