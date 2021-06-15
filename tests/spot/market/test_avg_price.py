from binance.spot import Spot as Client
import responses

from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}


def test_avg_price_without_symbol():
    """Tests the API endpoint to get avg price without symbol"""

    api = Client()
    api.avg_price.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/api/v3/avgPrice\\?symbol=BTCUSDT", mock_item, 200)
def test_avg_price():
    """Tests the API endpoint to avg price"""

    api = Client()
    response = api.avg_price("BTCUSDT")
    response.should.equal(mock_item)
