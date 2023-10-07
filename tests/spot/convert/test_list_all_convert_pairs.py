import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"fromAsset": "BTC", "toAsset": "USDT"}
expected_params = {"fromAsset": "BTC", "toAsset": "USDT"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/convert/exchangeInfo\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_list_all_convert_pairs():
    """Tests the API endpoint to list all convert pairs"""

    client = Client(key, secret)
    response = client.list_all_convert_pairs(**send_params)
    response.should.equal(mock_item)
