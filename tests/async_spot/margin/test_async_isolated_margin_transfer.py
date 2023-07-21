import pytest

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()

param = {
    "asset": "BTC",
    "symbol": "BTCUSDT",
    "transFrom": "SPOT",
    "transTo": "ISOLATED_MARGIN",
    "amount": "1",
}

@pytest.mark.asyncio
async def test_isolated_margin_transfer_without_asset():
    """Tests the API endpoint to transfer isolated margin without asset"""

    params = {
        "asset": "",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    try:
        response = await client.isolated_margin_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_isolated_margin_transfer_without_symbol():
    """Tests the API endpoint to transfer isolated margin without symbol"""

    params = {
        "asset": "USDT",
        "symbol": "",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    try:
        response = await client.isolated_margin_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_isolated_margin_transfer_without_transForm():
    """Tests the API endpoint to transfer isolated margin without transForm"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    try:
        response = await client.isolated_margin_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_isolated_margin_transfer_without_transTo():
    """Tests the API endpoint to transfer isolated margin without transTo"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "",
        "amount": "1",
    }
    client = Client(key, secret)
    try:
        response = await client.isolated_margin_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)


@pytest.mark.asyncio
async def test_isolated_margin_transfer_without_amount():
    """Tests the API endpoint to transfer isolated margin without amount"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "",
    }
    client = Client(key, secret)
    try:
        response = await client.isolated_margin_transfer(**params)
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "POST",
    "/sapi/v1/margin/isolated/transfer\\?" + urlencode(param),
    mock_item,
    200,
)
async def test_isolated_margin_transfer():
    """Tests the API endpoint to transfer isolated margin"""

    client = Client(key, secret)
    response = await client.isolated_margin_transfer(**param)
    response.should.equal(mock_item)
