import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

client = Client(key, secret)


def test_mining_account_earning_without_algo():
    """Tests the API endpoint to get account earnings without algo"""

    client.mining_account_earning.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/mining/payment/uid\\?algo=sha256", mock_item, 200
)
def test_mining_account_earning():
    """Tests the API endpoint to get account earnings"""

    client.mining_account_earning(algo="sha256").should.equal(mock_item)
