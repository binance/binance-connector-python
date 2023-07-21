from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterTypeError, ParameterArgumentError
import pytest
from urllib.parse import urlencode

from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "BNBUSDT"]'}


@pytest.mark.asyncio
@mock_async_http_response("GET", "/api/v3/ticker/bookTicker", mock_item, 200)
async def test_book_ticker_without_pair():
    """Tests the API endpoint to get book ticker from all pairs"""

    api = Client()
    response = await api.book_ticker()
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/ticker/bookTicker\\?symbol=BTCUSDT", mock_item, 200
)
async def test_book_ticker_single_symbol():
    """Tests the API endpoint to get book ticker of one pair"""

    api = Client()
    response = await api.book_ticker("BTCUSDT")
    response.should.equal(mock_item)


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/api/v3/ticker/bookTicker\\?" + urlencode(params), mock_item, 200
)
async def test_book_ticker_multiple_symbols():
    """Tests the API endpoint to get book tickers of multiple pairs"""

    api = Client()
    symbols = ["BTCUSDT", "BNBUSDT"]
    response = await api.book_ticker(symbols=symbols)
    response.should.equal(mock_item)

@pytest.mark.asyncio
async def test_book_ticker_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"BTCUSDT", "BNBUSDT"}
    try:
        response = await api.book_ticker(symbols=symbols)
    except Exception as e:
        assert isinstance(e, ParameterTypeError)
    else:
        assert isinstance(response, ParameterTypeError)

@pytest.mark.asyncio
async def test_book_ticker_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "ETHUSDT"
    symbols = ["BTCUSDT", "BNBUSDT"]
    try:
        response = await api.book_ticker(symbol=symbol, symbols=symbols)
    except Exception as e:
        assert isinstance(e, ParameterArgumentError)
    else:
        assert isinstance(response, ParameterArgumentError)

