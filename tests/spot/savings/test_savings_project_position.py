import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_fixed_activity_project_position_without_asset():
    """Tests the API endpoint to purchase Fixed/Activity project position without asset"""

    client = Client(key, secret)
    client.savings_project_position.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/lending/project/position/list\\?asset=1", mock_item, 200
)
def test_savings_fixed_activity_project():
    """Tests the API endpoint to purchase Fixed/Activity project position"""

    client = Client(key, secret)
    response = client.savings_project_position(asset=1)
    response.should.equal(mock_item)
