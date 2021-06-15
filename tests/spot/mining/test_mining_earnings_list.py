import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_mining_earnings_list_without_algo():
    """Tests the API endpoint to get earnings list without algo"""

    client = Client(key, secret)
    client.mining_earnings_list.when.called_with("", "test_name").should.throw(
        ParameterRequiredError
    )


def test_mining_earnings_list_without_username():
    """Tests the API endpoint to get earnings list without username"""

    client = Client(key, secret)
    client.mining_earnings_list.when.called_with("sha256", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/mining/payment/list\\?algo=sha256&userName=user_name",
    mock_item,
    200,
)
def test_mining_earnings_list():
    """Tests the API endpoint to get earnings list"""

    client = Client(key, secret)
    response = client.mining_earnings_list("sha256", "user_name")
    response.should.equal(mock_item)
