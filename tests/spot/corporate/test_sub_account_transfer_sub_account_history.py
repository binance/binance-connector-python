import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {
    "asset": "BNB",
    "type": 1,
    "startTime": "1591142602820",
    "endTime": "1591142602820",
    "limit": 10,
    "recvWindow": 1000,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/transfer/subUserHistory\\?" + urlencode(params),
    mock_item,
    200,
)
def test_sub_account_transfer_to_sub():
    """Tests the API endpoint to transfer asset to sub account transfer history"""

    client = Client(key, secret)
    response = client.sub_account_transfer_sub_account_history(**params)
    response.should.equal(mock_item)
