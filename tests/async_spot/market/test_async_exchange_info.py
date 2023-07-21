import pytest

from binance.error import ParameterTypeError, ParameterArgumentError
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from urllib.parse import urlencode

mock_item = {"key_1": "value_1", "key_2": "value_2"}
symbols_params = {"symbols": '["BTCUSDT", "ETHUSDT", "BNBUSDT"]'}
permissions_params = {"permissions": '["MARGIN", "LEVERAGED"]'}

api = Client()


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/exchangeInfo", mock_item, 200)
async def test_exchange_info():
    """Tests the API endpoint to get exchange info"""

    api = Client()
    response = await api.exchange_info()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/exchangeInfo\\?symbol=BTCUSDT", mock_item, 200
)
async def test_exchange_info_one_symbol():
    """Tests the API endpoint to get exchange info with one symbol"""

    api = Client()
    symbol = "BTCUSDT"
    response = await api.exchange_info(symbol=symbol)
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/exchangeInfo\\?" + urlencode(symbols_params), mock_item, 200
)
async def test_exchange_info_multiple_symbols():
    """Tests the API endpoint to get exchange info with multiple symbols"""

    api = Client()
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    response = await api.exchange_info(symbols=symbols)
    response.should.equal(mock_item)

@pytest.mark.asyncio
async def test_exchange_info_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"symbol1", "symbol2", "symbol3"}
    try:
        response = await api.exchange_info(symbols=symbols)
    except Exception as e:
        assert isinstance(e, ParameterTypeError)
    else:
        assert isinstance(response, ParameterTypeError)


@pytest.mark.asyncio
async def test_exchange_info_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "symbol"
    symbols = ["symbol1", "symbol2", "symbol3"]
    permissions = ["MARGIN", "LEVERAGED"]
    try:
        response = await api.exchange_info(symbol=symbol, symbols=symbols)
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)
    try:
        response = await api.exchange_info(
            permissions=permissions, symbols=symbols
        )
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)
    try:
        response = await api.exchange_info(
            permissions=permissions, symbol=symbol
        )
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/exchangeInfo\\?" + urlencode(permissions_params),
    mock_item,
    200,
)
async def test_exchange_info_with_permissions():
    """Tests the API endpoint with permissions"""

    permissions = ["MARGIN", "LEVERAGED"]
    response = await api.exchange_info(permissions=permissions)
    response.should.equal(mock_item)

@pytest.mark.asyncio
async def test_exchange_info_invalid_type_permissions():
    """Tests the API endpoint with invalid permissions data type"""

    try:
        response = await api.exchange_info(permissions="MARGIN")
    except Exception as e:
        assert isinstance(e, ParameterTypeError)
    else:
        assert isinstance(response, ParameterTypeError)

