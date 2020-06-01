import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()


def test_savings_purchase_customized_project_without_type():
    """ Tests the API endpoint to post customized fixed project without type """

    client = Client(key, secret)
    client.savings_purchase_customized_project.when.called_with(
        '').should.throw(ParameterRequiredError)


@mock_http_response(responses.POST, '/sapi/v1/lending/customizedFixed/purchase\\?type=1', mock_item, 200)
def test_savings_purchase_customized_project():
    """ Tests the API endpoint to post customized fixed project """

    client = Client(key, secret)
    response = client.savings_purchase_customized_project(type=1)
    response.should.equal(mock_item)
