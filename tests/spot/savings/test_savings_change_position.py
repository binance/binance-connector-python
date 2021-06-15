import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_change_fixed_activity_position_to_daily_position_without_projectId():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position without projectId"""

    client = Client(key, secret)
    client.savings_change_position.when.called_with("", "1").should.throw(
        ParameterRequiredError
    )


def test_change_fixed_activity_position_to_daily_position_without_lot():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position without lot"""

    client = Client(key, secret)
    client.savings_change_position.when.called_with("USDT001", None).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/positionChanged\\?projectId=USDT001&lot=1",
    mock_item,
    200,
)
def test_change_fixed_activity_position_to_daily_position():
    """Tests the API endpoint to change Fixed/Activity Position to Daily Position"""

    client = Client(key, secret)
    response = client.savings_change_position(projectId="USDT001", lot="1")
    response.should.equal(mock_item)
