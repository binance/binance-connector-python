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


def test_ratio_without_symbol():
    """Tests the API endpoint to get volume ratio without symbol"""

    client.ratio.when.called_with(symbol="", period="1m").should.throw(
        ParameterRequiredError
    )


def test_ratio_without_period():
    """Tests the API endpoint to get the volume ratio without interval"""

    client.ratio.when.called_with(symbol="BTCUSDT", period="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/futures/data/globalLongShortAccountRatio\\?symbol=BTCUSDT&period=1h", mock_item, 200
)
def test_ratio_with_default_limit():
    """Tests the API endpoint to get the volume ratio with default limit"""

    response = client.ratio(symbol="BTCUSDT", period="1h")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/futures/data/globalLongShortAccountRatio\\?symbol=BTCUSDT&period=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_ratio_with_given_params():
    """Tests the API endpoint to get the volume ratio with given parameters"""

    response = client.ratio(
        symbol="BTCUSDT", period="1h", limit=10, startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
