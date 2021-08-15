import responses

from tests.util import mock_http_response
from tests.util import random_id
from tests.util import timestamp
from binance.futures import Futures as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()


def test_agg_trades_without_symbol():
    """Tests the API endpoint to get old trades without symbol"""

    api = Client()
    api.agg_trades.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/fapi/v1/aggTrades\\?symbol=BTCUSDT", mock_item, 200)
def test_agg_trades_with_default_limit():
    """Tests the API endpoint to get agg trades by default limit"""

    api = Client()
    response = api.agg_trades("BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/fapi/v1/aggTrades\\?symbol=BTCUSDT&limit=1000", mock_item, 200
)
def test_agg_trades_with_limit_1000():
    """Tests the API endpoint to get agg trades with given limit"""

    api = Client()
    response = api.agg_trades("BTCUSDT", limit=1000)
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/aggTrades\\?symbol=BTCUSDT&fromId=" + str(fromId),
    mock_item,
    200,
)
def test_agg_trades_with_form_id():
    """Tests the API endpoint to get agg trades with formId"""

    api = Client()
    response = api.agg_trades("BTCUSDT", fromId=fromId)
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/aggTrades\\?symbol=BTCUSDT&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_agg_trades_with_timestamp():
    """Tests the API endpoint to get agg trades with specific timestamp"""

    api = Client()
    response = api.agg_trades("BTCUSDT", startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
