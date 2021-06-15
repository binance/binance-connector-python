import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()

params = {"coin": "BTC", "startTime": "1597130241000"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/futures/loan/borrow/history\\?" + urlencode(params),
    mock_item,
    200,
)
def test_futures_transfer_history():
    """Tests the API endpoint to get load borrow history"""

    client = Client(key, secret)
    response = client.futures_loan_borrow_history(**params)
    response.should.equal(mock_item)
