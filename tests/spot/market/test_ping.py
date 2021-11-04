from binance.spot import Spot as Client
import responses

from tests.util import mock_http_response


@mock_http_response(responses.GET, "/api/v3/ping", {}, 200)
def test_ping():
    """Tests the API endpoint to get connectivity"""

    api = Client()
    response = api.ping()
    response.should.equal({})
