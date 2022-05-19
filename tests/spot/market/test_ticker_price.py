from binance.spot import Spot as Client
import responses

from tests.util import mock_http_response
from urllib.parse import urlencode

mock_item = {"key_1": "value_1", "key_2": "value_2"}
params = {"symbols": '["BTCUSDT", "ETHUSDT", "BNBUSDT"]'}


@mock_http_response(responses.GET, "/api/v3/ticker/price", mock_item, 200)
def test_ticker_price_without_pair():
    """Tests the API endpoint to get price ticker from all pairs"""

    api = Client()
    response = api.ticker_price()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/price\\?symbol=BTCUSDT", mock_item, 200
)
def test_ticker_price_one_symbol():
    """Tests the API endpoint to get price ticker from one pair with one symbol"""

    api = Client()
    symbol = "BTCUSDT"
    response = api.ticker_price(symbol=symbol)
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/price\\?" + urlencode(params), mock_item, 200
)
def test_ticker_price_multiple_symbols():
    """Tests the API endpoint to get price ticker from one pair with one symbol"""

    api = Client()
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    response = api.ticker_price(symbols=symbols)
    response.should.equal(mock_item)
