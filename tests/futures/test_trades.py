from binance.futures import Futures as Client
import responses

from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}


def test_trades_without_symbol():
    """Tests the API endpoint to get recent trade list without symbol"""

    api = Client()
    api.trades.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/fapi/v1/trades\\?symbol=BTCUSDT", mock_item, 200)
def test_trades_with_default_limit():
    """Tests the API endpoint to get recent trades with default limit"""

    api = Client()
    response = api.trades("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/fapi/v1/trades\\?symbol=BTCUSDT&limit=1000", mock_item, 200
)
def test_trades_with_limit_1000():
    """Tests the API endpoint to get recent trades with given limit"""

    api = Client()
    response = api.trades("BTCUSDT", limit=1000)
    response.should.equal(mock_item)
