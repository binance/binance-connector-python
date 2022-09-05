from binance.spot import Spot as Client
from binance.error import ParameterTypeError, ParameterArgumentError
from urllib.parse import urlencode
import responses

from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "BNBUSDT"]'}


@mock_http_response(responses.GET, "/api/v3/ticker/24hr", mock_item, 200)
def test_ticker_24hr_without_pair():
    """Tests the API endpoint to get 24hr ticker from all pairs"""

    api = Client()
    response = api.ticker_24hr()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/24hr\\?symbol=BTCUSDT", mock_item, 200
)
def test_avg_price_single_symbol():
    """Tests the API endpoint to get ticker of one pair"""

    api = Client()
    response = api.ticker_24hr("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/24hr\\?" + urlencode(params), mock_item, 200
)
def test_avg_price_multiple_symbols():
    """Tests the API endpoint to get tickers of multiple pairs"""

    api = Client()
    symbols = ["BTCUSDT", "BNBUSDT"]
    response = api.ticker_24hr(symbols=symbols)
    response.should.equal(mock_item)


def test_avg_price_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"BTCUSDT", "BNBUSDT"}
    api.ticker_24hr.when.called_with(symbols=symbols).should.throw(ParameterTypeError)


def test_avg_price_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "ETHUSDT"
    symbols = ["BTCUSDT", "BNBUSDT"]
    api.ticker_24hr.when.called_with(symbol=symbol, symbols=symbols).should.throw(
        ParameterArgumentError
    )


@mock_http_response(
    responses.GET,
    "/api/v3/ticker/24hr\\?symbol=BTCUSDT&type=MINI",
    mock_item,
    200,
)
def test_rolling_window_ticker_with_given_params():
    """Tests the API endpoint to get ticker with given parameters"""

    api = Client()
    response = api.ticker_24hr(symbol="BTCUSDT", symbols=None, type="MINI")
    response.should.equal(mock_item)
