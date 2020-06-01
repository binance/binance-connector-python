import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()


def test_sub_account_futures_position_risk_without_email():
    """ Tests the API endpoint to get sub account futures postion risk without email """

    client = Client(key, secret)
    client.sub_account_futures_position_risk.when.called_with(
        '').should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, '/sapi/v1/sub-account/futures/positionRisk\\?email=alice@test.com', mock_item, 200)
def test_sub_account_futures_position_risk():
    """ Tests the API endpoint to get sub account futures postion risk """

    client = Client(key, secret)
    response = client.sub_account_futures_position_risk(email='alice@test.com')
    response.should.equal(mock_item)
