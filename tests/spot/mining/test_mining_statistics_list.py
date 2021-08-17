import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_mining_statistics_list_without_algo():
    """Tests the API endpoint to get statistics list without algo"""

    client = Client(key, secret)
    client.mining_statistics_list.when.called_with("", "test_name").should.throw(
        ParameterRequiredError
    )


def test_mining_statistics_list_without_username():
    """Tests the API endpoint to get statistics list without username"""

    client = Client(key, secret)
    client.mining_statistics_list.when.called_with("sha256", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/mining/statistics/user/status\\?algo=sha256&userName=user_name",
    mock_item,
    200,
)
def test_mining_statistics():
    """Tests the API endpoint to get statistics list"""

    client = Client(key, secret)
    response = client.mining_statistics_list("sha256", "user_name")
    response.should.equal(mock_item)
