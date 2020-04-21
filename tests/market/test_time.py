import sure
import binance
import responses

from tests.util import mock_http_response

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

@mock_http_response(responses.GET, '/api/v3/time', mock_item, 200)
def test_time():
    """ Tests the API endpoint to get exchange time """

    api =  binance.API()
    response = api.time()
    response.json().should.equal(mock_item)
