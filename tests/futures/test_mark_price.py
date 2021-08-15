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
    "/fapi/v1/premiumIndex",
    mock_item,
    200,
)
def test_mark_price_without_symbol():
    """Tests the API endpoint to get mark price without symbol"""

    response = client.mark_price(
        symbol="BTCUSDT")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/fapi/v1/premiumIndex\\?symbol=BTCUSDT",
    mock_item,
    200,
)
def test_mark_price_with_given_params():
    """Tests the API endpoint to get mark price with given parameters"""

    response = client.mark_price(
        symbol="BTCUSDT")
    response.should.equal(mock_item)
