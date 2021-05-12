import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError, ClientError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

key = random_str()
secret = random_str()


params = {
    'startTime': '1591142602820',
    'endTime': '1591142602820',
    'page': 1,
    'limit': 100,
    'recvWindow': 1000
}


def test_sub_account_transfer_history_without_email():
    """ Tests the API endpoint to get transfer history without email """

    client = Client(key, secret)
    client.sub_account_transfer_history.when.called_with(
        '').should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, '/sapi/v1/sub-account/sub/transfer/history\\?email=alice@test.com&' + urlencode(params), mock_item, 200)
def test_sub_account_transfer_history():
    """ Tests the API endpoint to get transfer history """

    client = Client(key, secret)
    response = client.sub_account_transfer_history(email='alice@test.com', **params)
    response.should.equal(mock_item)
