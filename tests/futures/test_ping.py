from binance.futures import Futures as Client
import responses

from tests.util import mock_http_response


@mock_http_response(responses.GET, "/fapi/v1/ping", {}, 200)
def test_ping():
    """Tests the API endpoint to get connectivity"""

    api = Client()
    response = api.ping()
    response.should.equal({})
