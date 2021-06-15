import responses

from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}


def test_depth_without_symbol():
    """Tests the API endpoint to get exchange order book depth without symbol"""

    api = Client()
    api.depth.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/api/v3/depth\\?symbol=BTCUSDT", mock_item, 200)
def test_depth():
    """Tests the API endpoint to get exchange order book depth with default parameters"""

    api = Client()
    response = api.depth("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/depth\\?symbol=BTCUSDT&limit=10", mock_item, 200
)
def test_depth_fixed_limit():
    """Tests the API endpoint to get exchange order book depth with limit 10"""

    api = Client()
    response = api.depth("BTCUSDT", limit=10)
    response.should.equal(mock_item)
