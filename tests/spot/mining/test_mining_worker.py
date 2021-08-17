import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_mining_worker_without_algo():
    """Tests the API endpoint to get worker without algo"""

    client = Client(key, secret)
    client.mining_worker.when.called_with("", "test_name", "worker_name").should.throw(
        ParameterRequiredError
    )


def test_mining_worker_without_username():
    """Tests the API endpoint to get worker without username"""

    client = Client(key, secret)
    client.mining_worker.when.called_with("sha256", "", "worker_name").should.throw(
        ParameterRequiredError
    )


def test_mining_worker_without_workername():
    """Tests the API endpoint to get worker without workername"""

    client = Client(key, secret)
    client.mining_worker.when.called_with("sha256", "test_name", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/mining/worker/detail\\?algo=sha256&userName=user_name&workerName=worker_name",
    mock_item,
    200,
)
def test_mining_worker():
    """Tests the API endpoint to get coin list"""

    client = Client(key, secret)
    response = client.mining_worker("sha256", "user_name", "worker_name")
    response.should.equal(mock_item)
