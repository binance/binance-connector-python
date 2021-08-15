import responses

from binance.futures import Futures as Client

from tests.util import mock_http_response
from tests.util import random_id
from tests.util import timestamp
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()
client = Client()


def test_open_interest_statistics_without_symbol():
    """Tests the API endpoint to get the open interest statistics without symbol"""

    client.open_interest_statistics.when.called_with(symbol="", period="1m").should.throw(
        ParameterRequiredError
    )


def test_open_interest_statistics_without_period():
    """Tests the API endpoint to get the open interest statistics without period"""

    client.open_interest_statistics.when.called_with(symbol="BTCUSDT", period="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/futures/data/openInterestHist\\?symbol=BTCUSDT&period=1h", mock_item, 200
)
def test_open_interest_statistics_with_default_limit():
    """Tests the API endpoint to get the open interest statistics with default limit"""

    response = client.open_interest_statistics(symbol="BTCUSDT", period="1h")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/futures/data/openInterestHist\\?symbol=BTCUSDT&period=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_open_interest_statistics_with_given_params():
    """Tests the API endpoint to get the open interest statistics with given parameters"""

    response = client.open_interest_statistics(
        symbol="BTCUSDT", period="1h", limit=10, startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
