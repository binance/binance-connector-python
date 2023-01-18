import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"orderId": 100000001}


@mock_http_response(
    responses.GET,
    "/sapi/v1/loan/vip/repay/history\\?" + urlencode(params),
    mock_item,
    200,
)
def test_loan_vip_repay_history():
    """Tests the API endpoint to get vip loan history"""

    response = client.loan_vip_repay_history(**params)
    response.should.equal(mock_item)
