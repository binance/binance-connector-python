from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterTypeError, ParameterArgumentError
from urllib.parse import urlencode
import pytest

from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "BNBUSDT"]'}
windowSize = "1d"


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/ticker\\?symbol=BTCUSDT", mock_item, 200)
async def test_rolling_window_ticker_single_symbol():
    """Tests the API endpoint to get ticker of one pair"""

    api = Client()
    response = await api.rolling_window_ticker("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/ticker\\?" + urlencode(params), mock_item, 200
)
async def test_rolling_window_ticker_multiple_symbols():
    """Tests the API endpoint to get tickers of multiple pairs"""

    api = Client()
    symbols = ["BTCUSDT", "BNBUSDT"]
    response = await api.rolling_window_ticker(symbols=symbols)
    response.should.equal(mock_item)

@pytest.mark.asyncio
async def test_rolling_window_ticker_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"BTCUSDT", "BNBUSDT"}
    try:
        response = await api.rolling_window_ticker(symbols=symbols)
    except Exception as e:
        assert isinstance(e, ParameterTypeError)
    else:
        assert isinstance(response, ParameterTypeError)


@pytest.mark.asyncio
async def test_rolling_window_ticker_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "ETHUSDT"
    symbols = ["BTCUSDT", "BNBUSDT"]
    try:
        response = await api.rolling_window_ticker(
            symbol=symbol, symbols=symbols
        )
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/api/v3/ticker\\?symbol=BTCUSDT&windowSize=" + str(windowSize) + "&type=MINI",
    mock_item,
    200,
)
async def test_rolling_window_ticker_with_given_params():
    """Tests the API endpoint to get ticker with given parameters"""

    client = Client()
    response = await client.rolling_window_ticker(
        symbol="BTCUSDT", windowSize=windowSize, type="MINI"
    )
    response.should.equal(mock_item)
