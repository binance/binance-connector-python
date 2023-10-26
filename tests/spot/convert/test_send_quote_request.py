import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "fromAsset": "BTC",
    "toAsset": "USDT",
    "fromAmount": 1,
    "toAmount": 1,
    "validTime": "10s",
    "walletType": "SPOT",
    "recvWindow": 5000,
}
expected_params = {
    "fromAsset": "BTC",
    "toAsset": "USDT",
    "fromAmount": 1,
    "toAmount": 1,
    "validTime": "10s",
    "walletType": "SPOT",
    "recvWindow": 5000,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/convert/getQuote\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_send_quote_request():
    """Tests the API endpoint to send quote request"""

    client = Client(key, secret)
    response = client.send_quote_request(**send_params)
    response.should.equal(mock_item)
