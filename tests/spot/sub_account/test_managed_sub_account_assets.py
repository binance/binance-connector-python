import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


params = {"email": "alice@test.com", "recvWindow": 1000}


def test_managed_sub_account_query_assets_without_email():
    """Tests the API endpoint to query asset from managed sub account without email"""

    params = {"email": "", "recvWindow": 1000}
    client = Client(key, secret)
    client.managed_sub_account_assets.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/managed-subaccount/asset\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_managed_sub_account_withdraw_assets():
    """Tests the API endpoint to query asset from managed sub account"""

    client = Client(key, secret)
    response = client.managed_sub_account_assets(**params)
    response.should.equal(mock_item)
