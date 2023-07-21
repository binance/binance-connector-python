import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()
listen_key = random_str()

@pytest.mark.asyncio
async def test_close_isolated_margin_listen_key_without_symbol():
    """Tests the API endpoint to close an isolated margin listen key without symbol"""

    param = {"symbol": "", "listenKey": listen_key}

    client = Client(key, secret)
    try:
        response = await client.close_isolated_margin_listen_key(**param)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_close_isolated_margin_listen_key_without_listen_key():
    """Tests the API endpoint to close an isolated margin listen key without listenkey"""

    param = {"symbol": "BTCUSDT", "listenKey": ""}
    client = Client(key, secret)
    try:
        response = await client.close_isolated_margin_listen_key(**param)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "DELETE",
    "/sapi/v1/userDataStream/isolated\\?listenKey=" + listen_key + "&symbol=BTCUSDT",
    mock_item,
    200,
)
async def test_close_isolated_margin_listen_key():
    """Tests the API endpoint to close an isolated margin listen key"""

    client = Client(key)
    response = await client.close_isolated_margin_listen_key(
        symbol="BTCUSDT", listenKey=listen_key
    )
    response.should.equal(mock_item)
