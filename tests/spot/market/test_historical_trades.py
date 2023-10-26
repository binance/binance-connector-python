import responses

from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

fromId = "123456789"


def test_historical_trades_without_symbol():
    """Tests the API endpoint to get old trades without symbol"""

    api = Client()
    api.historical_trades.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/api/v3/historicalTrades\\?symbol=BTCUSDT", mock_item, 200
)
def test_historical_trades_with_default_params():
    """Tests the API endpoint to get old trades by default params"""

    api = Client()
    response = api.historical_trades("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/api/v3/historicalTrades\\?symbol=BTCUSDT&limit=1000&fromId=" + fromId,
    mock_item,
    200,
)
def test_historical_trades_with_provide_params():
    """Tests the API endpoint to get recent trades with given limit"""

    api = Client()
    response = api.historical_trades("BTCUSDT", limit=1000, fromId=fromId)
    response.should.equal(mock_item)
