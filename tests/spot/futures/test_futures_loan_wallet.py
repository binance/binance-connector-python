import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v2/futures/loan/wallet", mock_item, 200)
def test_futures_loan_wallet():
    """Tests the API endpoint to get loan wallet"""

    client = Client(key, secret)
    response = client.futures_loan_wallet()
    response.should.equal(mock_item)
