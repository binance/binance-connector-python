import responses

from binance.futures import Futures as Client

from tests.util import mock_http_response
from tests.util import random_id
from tests.util import timestamp

mock_item = {"key_1": "value_1", "key_2": "value_2"}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()
client = Client()


@mock_http_response(
    responses.GET,
    "/fapi/v1/ticker/bookTicker",
    mock_item,
    200,
)
def test_book_ticker_without_params():
    """Tests the API endpoint to get book ticker without parameters"""

    response = client.book_ticker()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/ticker/bookTicker\\?symbol=BTCUSDT",
    mock_item,
    200,
)
def test_book_ticker_with_given_params():
    """Tests the API endpoint to get book ticker with given parameters"""

    response = client.book_ticker(symbol="BTCUSDT")
    response.should.equal(mock_item)
