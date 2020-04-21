import sure
import binance
import responses

from tests.util import mock_http_response

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

@mock_http_response(responses.GET, '/api/v3/ticker/bookTicker', mock_item, 200)
def test_book_ticker_without_pair():
    """ Tests the API endpoint to get book ticker from all pairs """

    api = binance.API()
    response = api.book_ticker()
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/ticker/bookTicker\\?symbol=BTCUSDT', mock_item, 200)
def test_book_ticker():
    """ Tests the API endpoint to get book ticker from one pair """

    api = binance.API()
    response = api.book_ticker('BTCUSDT')
    response.json().should.equal(mock_item)
