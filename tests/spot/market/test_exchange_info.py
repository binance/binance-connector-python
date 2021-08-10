import responses

from binance.error import ParameterTypeError
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}


@mock_http_response(responses.GET, "/api/v3/exchangeInfo", mock_item, 200)
def test_exchange_info():
    """Tests the API endpoint to get exchange info"""

    api = Client()
    response = api.exchange_info()
    response.should.equal(mock_item)


@mock_http_response(responses.GET, "/api/v3/exchangeInfo", mock_item, 200)
def test_exchange_info_one_symbol():
    """Tests the API endpoint to get exchange info with one symbol"""

    api = Client()
    symbol = "symbol"
    response = api.exchange_info(symbol=symbol)
    response.should.equal(mock_item)


@mock_http_response(responses.GET, "/api/v3/exchangeInfo", mock_item, 200)
def test_exchange_info_multiple_symbols():
    """Tests the API endpoint to get exchange info with multiple symbols"""

    api = Client()
    symbols = ["symbol1", "symbol2", "symbol3"]
    response = api.exchange_info(symbols=symbols)
    response.should.equal(mock_item)


def test_exchange_info_invalid_type_symbols():
    """Tests the API endpoint with invalid symbols data type"""

    api = Client()
    symbols = {"symbol1", "symbol2", "symbol3"}
    api.exchange_info.when.called_with(
        symbols=symbols
    ).should.throw(ParameterTypeError)
