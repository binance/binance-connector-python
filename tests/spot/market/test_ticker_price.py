from binance.spot import Spot as Client
import responses

from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}


@mock_http_response(responses.GET, "/api/v3/ticker/price", mock_item, 200)
def test_ticker_price_without_pair():
    """Tests the API endpoint to get price ticker from all pairs"""

    api = Client()
    response = api.ticker_price()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/ticker/price\\?symbol=BTCUSDT", mock_item, 200
)
def test_ticker_price():
    """Tests the API endpoint to get price ticker from one pair"""

    api = Client()
    response = api.ticker_price("BTCUSDT")
    response.should.equal(mock_item)
