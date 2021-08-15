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


def test_continuous_kline_without_pair():
    """Tests the API endpoint to get continuous klines without pair"""

    client.continuous_klines.when.called_with(pair="", interval="1m", contract_type="PERPETUAL").should.throw(
        ParameterRequiredError
    )


def test_continuous_kline_without_interval():
    """Tests the API endpoint to get continuous kline without interval"""

    client.continuous_klines.when.called_with(pair="BTCUSDT", interval="", contract_type="PERPETUAL").should.throw(
        ParameterRequiredError
    )


def test_continuous_kline_without_contract_type():
    """Tests the API endpoint to get continuous kline without contract type"""

    client.continuous_klines.when.called_with(pair="BTCUSDT", interval="", contract_type="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/fapi/v1/continuousKlines\\?pair=BTCUSDT&contractType=PERPETUAL&interval=1h", mock_item, 200
)
def test_continuous_kline_with_default_limit():
    """Tests the API endpoint to get continuous kline with default limit"""

    response = client.continuous_klines(pair="BTCUSDT", interval="1h", contract_type="PERPETUAL")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/continuousKlines\\?pair=BTCUSDT&contractType=PERPETUAL&interval=1h&limit=10&startTime="
    + str(startTime)
    + "&endTime="
    + str(endTime),
    mock_item,
    200,
)
def test_continuous_kline_with_given_params():
    """Tests the API endpoint to get continuous klines with given parameters"""

    response = client.continuous_klines(
        pair="BTCUSDT", contract_type="PERPETUAL", interval="1h", limit=10, startTime=startTime, endTime=endTime)
    response.should.equal(mock_item)
