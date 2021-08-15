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


def test_top_traders_positions_without_symbol():
    """Tests the API endpoint to get top traders positions without symbol"""

    client.top_trader_positions.when.called_with(symbol="", period="1m").should.throw(
        ParameterRequiredError
    )


def test_top_traders_positions_without_period():
    """Tests the API endpoint to get top traders positions without interval"""

    client.top_trader_positions.when.called_with(symbol="BTCUSDT", period="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/futures/data/topLongShortPositionRatio\\?symbol=BTCUSDT&period=1h", mock_item, 200
)
def test_top_traders_positions_with_default_limit():
    """Tests the API endpoint to get top traders positions with default limit"""

    response = client.top_trader_positions(symbol="BTCUSDT", period="1h")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/futures/data/topLongShortPositionRatio\\?symbol=BTCUSDT&period=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_top_traders_positions_with_given_params():
    """Tests the API endpoint to get top traders positions with given parameters"""

    response = client.top_trader_positions(
        symbol="BTCUSDT", period="1h", limit=10, startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
