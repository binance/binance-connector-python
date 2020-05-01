import sure
import binance
import responses

from tests.util import mock_http_response


@mock_http_response(responses.GET, '/api/v3/ping', {}, 200)
def test_ping():
    """ Tests the API endpoint to get conectivity """

    api = binance.Market()
    response = api.ping()
    response.should.equal({})
