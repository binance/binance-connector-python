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


def test_open_interest_without_symbol():
    """Tests the API endpoint to get open interest without symbol"""

    client.open_interest.when.called_with(symbol="").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/fapi/v1/openInterest\\?symbol=BTCUSDT",
    mock_item,
    200,
)
def test_open_interest_with_given_params():
    """Tests the API endpoint to get open interest with given parameters"""

    response = client.open_interest(symbol="BTCUSDT")
    response.should.equal(mock_item)
