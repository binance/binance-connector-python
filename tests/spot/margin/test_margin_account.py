import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/margin/account", mock_item, 200)
def test_margin_account():
    """Tests the API endpoint to margin account information"""

    client = Client(key, secret)
    response = client.margin_account()
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/account\\?recvWindow=10000", mock_item, 200
)
def test_margin_account_with_recvWindow():
    """Tests the API endpoint to margin account information with recvWindow"""

    client = Client(key, secret)
    response = client.margin_account(recvWindow=10000)
    response.should.equal(mock_item)
