from binance.spot import Spot as Client
from binance.error import ParameterTypeError, ParameterArgumentError
from urllib.parse import urlencode
import responses

from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "BNBUSDT"]'}
windowSize = "1d"


@mock_http_response(responses.GET, "/api/v3/ticker\\?symbol=BTCUSDT", mock_item, 200)
def test_rolling_window_ticker_single_symbol():
    """Tests the API endpoint to get ticker of one pair"""

    api = Client()
    response = api.rolling_window_ticker("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker\\?" + urlencode(params), mock_item, 200
)
def test_rolling_window_ticker_multiple_symbols():
    """Tests the API endpoint to get tickers of multiple pairs"""

    api = Client()
    symbols = ["BTCUSDT", "BNBUSDT"]
    response = api.rolling_window_ticker(symbols=symbols)
    response.should.equal(mock_item)


def test_rolling_window_ticker_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"BTCUSDT", "BNBUSDT"}
    api.rolling_window_ticker.when.called_with(symbols=symbols).should.throw(
        ParameterTypeError
    )


def test_rolling_window_ticker_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "ETHUSDT"
    symbols = ["BTCUSDT", "BNBUSDT"]
    api.rolling_window_ticker.when.called_with(
        symbol=symbol, symbols=symbols
    ).should.throw(ParameterArgumentError)


@mock_http_response(
    responses.GET,
    "/api/v3/ticker\\?symbol=BTCUSDT&windowSize=" + str(windowSize) + "&type=MINI",
    mock_item,
    200,
)
def test_rolling_window_ticker_with_given_params():
    """Tests the API endpoint to get ticker with given parameters"""

    client = Client()
    response = client.rolling_window_ticker(
        symbol="BTCUSDT", windowSize=windowSize, type="MINI"
    )
    response.should.equal(mock_item)
