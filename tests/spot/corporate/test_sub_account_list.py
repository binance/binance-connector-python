import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1"}

key = random_str()
secret = random_str()

params = {"isFreeze": "false", "page": 1, "limit": 100, "recvWindow": 1000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/list\\?email=alice@test.com&" + urlencode(params),
    mock_item,
    200,
)
def test_sub_account_list():
    """Tests the API endpoint to query sub account list"""

    client = Client(key, secret)
    response = client.sub_account_list(email="alice@test.com", **params)
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/sapi/v1/sub-account/list\\?" + urlencode(params), mock_item, 200
)
def test_sub_account_list_without_email():
    """Tests the API endpoint to query sub account list"""

    client = Client(key, secret)
    response = client.sub_account_list(**params)
    response.should.equal(mock_item)
