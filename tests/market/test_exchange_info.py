import sure
from binance.market import Market
import responses

from tests.util import mock_http_response

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}


@mock_http_response(responses.GET, '/api/v3/exchangeInfo', mock_item, 200)
def test_exchange_info():
    """ Tests the API endpoint to get exchange info """

    api = Market()
    response = api.exchange_info()
    response.should.equal(mock_item)
