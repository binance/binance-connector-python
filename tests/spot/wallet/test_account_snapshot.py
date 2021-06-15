import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_account_snapshot_without_type():
    """Tests the API endpoint to get account snapshot without type"""

    client = Client(key, secret)
    client.account_snapshot.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/accountSnapshot\\?type=SPOT", mock_item, 200
)
def test_account_snapshot():
    """Tests the API endpoint to get account snapshot"""

    client = Client(key, secret)
    response = client.account_snapshot(type="SPOT")
    response.should.equal(mock_item)
