import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_project_list_without_type():
    """Tests the API endpoint to get Fixed and Activity Project without type"""

    client = Client(key, secret)
    client.savings_project_list.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/lending/project/list\\?type=1", mock_item, 200
)
def test_savings_project_list():
    """Tests the API endpoint to get Fixed and Activity Project"""

    client = Client(key, secret)
    response = client.savings_project_list(type=1)
    response.should.equal(mock_item)
