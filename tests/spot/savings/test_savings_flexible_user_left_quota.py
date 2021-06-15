import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_flexible_user_left_quota_without_productId():
    """Tests the API endpoint to get left daily purchase quota of flexible product without productId"""

    client = Client(key, secret)
    client.savings_flexible_user_left_quota.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/lending/daily/userLeftQuota\\?productId=1", mock_item, 200
)
def test_savings_flexible_user_left_quota():
    """Tests the API endpoint to get left daily purchase quota of flexible product"""

    client = Client(key, secret)
    response = client.savings_flexible_user_left_quota(productId=1)
    response.should.equal(mock_item)
