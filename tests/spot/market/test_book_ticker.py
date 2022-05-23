from binance.spot import Spot as Client
from binance.error import ParameterTypeError, ParameterArgumentError
import responses
from urllib.parse import urlencode

from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "BNBUSDT"]'}


@mock_http_response(responses.GET, "/api/v3/ticker/bookTicker", mock_item, 200)
def test_book_ticker_without_pair():
    """Tests the API endpoint to get book ticker from all pairs"""

    api = Client()
    response = api.book_ticker()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/bookTicker\\?symbol=BTCUSDT", mock_item, 200
)
def test_book_ticker_single_symbol():
    """Tests the API endpoint to get book ticker of one pair"""

    api = Client()
    response = api.book_ticker("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/bookTicker\\?" + urlencode(params), mock_item, 200
)
def test_book_ticker_multiple_symbols():
    """Tests the API endpoint to get book tickers of multiple pairs"""

    api = Client()
    symbols = ["BTCUSDT", "BNBUSDT"]
    response = api.book_ticker(symbols=symbols)
    response.should.equal(mock_item)


def test_book_ticker_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"BTCUSDT", "BNBUSDT"}
    api.book_ticker.when.called_with(symbols=symbols).should.throw(ParameterTypeError)


def test_book_ticker_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "ETHUSDT"
    symbols = ["BTCUSDT", "BNBUSDT"]
    api.book_ticker.when.called_with(symbol=symbol, symbols=symbols).should.throw(
        ParameterArgumentError
    )
