import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"asset": "BTC", "size": 100, "recvWindow": 5000}
expected_params = {"asset": "BTC", "size": 100, "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/portfolio/interest-history\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_classic_portfolio_margin_negative_balance_interest_history():
    """Tests the API endpoint to query classic portfolio margin negative balance interest history"""

    client = Client(key, secret)
    response = client.query_classic_portfolio_margin_negative_balance_interest_history(
        **send_params
    )
    response.should.equal(mock_item)
