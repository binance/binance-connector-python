import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_purchase_fixed_activity_project_without_projectId():
    """Tests the API endpoint to purchase Fixed/Activity Project without projectId"""

    client = Client(key, secret)
    client.savings_purchase_project.when.called_with("", 1).should.throw(
        ParameterRequiredError
    )


def test_savings_purchase_fixed_activity_project_without_lot():
    """Tests the API endpoint to purchase Fixed/Activity Project without without lot"""

    client = Client(key, secret)
    client.savings_purchase_project.when.called_with(
        "CUSDT14DAYSS001", None
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/customizedFixed/purchase\\?projectId=CUSDT14DAYSS001&lot=1",
    mock_item,
    200,
)
def test_savings_purchase_fixed_activity_project():
    """Tests the API endpoint to purchase Fixed/Activity Project"""

    client = Client(key, secret)
    response = client.savings_purchase_project(projectId="CUSDT14DAYSS001", lot=1)
    response.should.equal(mock_item)
