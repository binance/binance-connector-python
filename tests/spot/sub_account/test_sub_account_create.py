import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1"}

key = random_str()
secret = random_str()

params = {"subAccountString": "virtual.account", "recvWindow": 1000}


def test_sub_account_create_without_sub_account_string():
    """Tests the API endpoint to create sub-account without subAccountString"""

    client = Client(key, secret)
    client.sub_account_create.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/virtualSubAccount\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_create():
    """Tests the API endpoint to create sub-account"""

    client = Client(key, secret)
    response = client.sub_account_create(**params)
    response.should.equal(mock_item)
