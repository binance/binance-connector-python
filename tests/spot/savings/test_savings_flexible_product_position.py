import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()


def test_savings_flexible_product_position_without_asset():
    """ Tests the API endpoint to get flexible product position without asset """

    client = Client(key, secret)
    client.savings_flexible_product_position.when.called_with(
        '').should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, '/sapi/v1/lending/daily/token/position\\?asset=1', mock_item, 200)
def test_savings_flexible_user_redemption_quota():
    """ Tests the API endpoint to get flexible redemption quota """

    client = Client(key, secret)
    response = client.savings_flexible_product_position(asset=1)
    response.should.equal(mock_item)