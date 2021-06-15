import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_sub_account_margin_account_without_email():
    """Tests the API endpoint to get sub account margin account without email"""

    client = Client(key, secret)
    client.sub_account_margin_account.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/margin/account\\?email=alice@test.com",
    mock_item,
    200,
)
def test_sub_account_margin_account():
    """Tests the API endpoint to get sub account margin account"""

    client = Client(key, secret)
    response = client.sub_account_margin_account(email="alice@test.com")
    response.should.equal(mock_item)
