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


def test_mark_price_kline_without_symbol():
    """Tests the API endpoint to get mark price klines without symbol"""

    client.mark_price_klines.when.called_with(symbol="", interval="1m").should.throw(
        ParameterRequiredError
    )


def test_mark_price_kline_without_interval():
    """Tests the API endpoint to get mark price klines without interval"""

    client.mark_price_klines.when.called_with(symbol="BTCUSDT", interval="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/fapi/v1/markPriceKlines\\?symbol=BTCUSDT&interval=1h", mock_item, 200
)
def test_mark_price_kline_with_default_limit():
    """Tests the API endpoint to get mark price klines with default limit"""

    response = client.mark_price_klines(symbol="BTCUSDT", interval="1h")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/markPriceKlines\\?symbol=BTCUSDT&interval=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_mark_price_kline_with_given_params():
    """Tests the API endpoint to get mark price klines with given parameters"""

    response = client.mark_price_klines(
        symbol="BTCUSDT", interval="1h", limit=10, startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
