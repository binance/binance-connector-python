import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"vipLevel": 1, "coin": "BNB"}

client = Client(key, secret)


@mock_http_response(responses.GET, "/sapi/v1/margin/crossMarginData", mock_item, 200)
def test_margin_fee_without_params():
    """Tests the API endpoint to get cross margin fee data without params"""

    response = client.margin_fee()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/crossMarginData\\?" + urlencode(params),
    mock_item,
    200,
)
def test_margin_fee():
    """Tests the API endpoint to get cross margin fee data"""

    response = client.margin_fee(**params)
    response.should.equal(mock_item)
