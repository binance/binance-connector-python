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


@mock_http_response(
    responses.GET,
    "/fapi/v1/indexInfo",
    mock_item,
    200,
)
def test_composite_index_without_params():
    """Tests the API endpoint to get composite index without given parameters"""

    response = client.composite_index()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/indexInfo\\?symbol=BTCUSDT",
    mock_item,
    200,
)
def test_composite_index_with_given_params():
    """Tests the API endpoint to get composite index with given parameters"""

    response = client.composite_index(symbol="BTCUSDT")
    response.should.equal(mock_item)
