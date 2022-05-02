import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {"email": "alice@test.com", "type": "SPOT"}


def test_managed_sub_account_get_snapshot_without_email():
    """Tests the API endpoint to query managed sub-account snapshot without email"""

    params = {"email": "", "type": "SPOT"}
    client = Client(key, secret)
    client.managed_sub_account_get_snapshot.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_managed_sub_account_get_snapshot_without_type():
    """Tests the API endpoint to query managed sub-account snapshot without type"""

    params = {"email": "alice@test.com", "type": ""}
    client = Client(key, secret)
    client.managed_sub_account_get_snapshot.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/managed-subaccount/accountSnapshot\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_managed_sub_account_get_snapshot():
    """Tests the API endpoint to query managed sub-account snapshot"""

    client = Client(key, secret)
    response = client.managed_sub_account_get_snapshot(**params)
    response.should.equal(mock_item)
