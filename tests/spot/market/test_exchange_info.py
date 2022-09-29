import responses

from binance.error import ParameterTypeError, ParameterArgumentError
from tests.util import mock_http_response
from binance.spot import Spot as Client
from urllib.parse import urlencode

mock_item = {"key_1": "value_1", "key_2": "value_2"}
symbols_params = {"symbols": '["BTCUSDT", "ETHUSDT", "BNBUSDT"]'}
permissions_params = {"permissions": '["MARGIN", "LEVERAGED"]'}

api = Client()


@mock_http_response(responses.GET, "/api/v3/exchangeInfo", mock_item, 200)
def test_exchange_info():
    """Tests the API endpoint to get exchange info"""

    api = Client()
    response = api.exchange_info()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/exchangeInfo\\?symbol=BTCUSDT", mock_item, 200
)
def test_exchange_info_one_symbol():
    """Tests the API endpoint to get exchange info with one symbol"""

    api = Client()
    symbol = "BTCUSDT"
    response = api.exchange_info(symbol=symbol)
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/exchangeInfo\\?" + urlencode(symbols_params), mock_item, 200
)
def test_exchange_info_multiple_symbols():
    """Tests the API endpoint to get exchange info with multiple symbols"""

    api = Client()
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    response = api.exchange_info(symbols=symbols)
    response.should.equal(mock_item)


def test_exchange_info_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"symbol1", "symbol2", "symbol3"}
    api.exchange_info.when.called_with(symbols=symbols).should.throw(ParameterTypeError)


def test_exchange_info_with_double_parameter():
    """Tests the API endpoint with double parameter"""

    api = Client()
    symbol = "symbol"
    symbols = ["symbol1", "symbol2", "symbol3"]
    permissions = ["MARGIN", "LEVERAGED"]
    api.exchange_info.when.called_with(symbol=symbol, symbols=symbols).should.throw(
        ParameterArgumentError
    )
    api.exchange_info.when.called_with(
        permissions=permissions, symbols=symbols
    ).should.throw(ParameterArgumentError)
    api.exchange_info.when.called_with(
        permissions=permissions, symbol=symbol
    ).should.throw(ParameterArgumentError)


@mock_http_response(
    responses.GET,
    "/api/v3/exchangeInfo\\?" + urlencode(permissions_params),
    mock_item,
    200,
)
def test_exchange_info_with_permissions():
    """Tests the API endpoint with permissions"""

    permissions = ["MARGIN", "LEVERAGED"]
    response = api.exchange_info(permissions=permissions)
    response.should.equal(mock_item)


def test_exchange_info_invalid_type_permissions():
    """Tests the API endpoint with invalid permissions data type"""

    api.exchange_info.when.called_with(permissions="MARGIN").should.throw(
        ParameterTypeError
    )
