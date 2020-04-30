import sure
import binance
import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError, APIException

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
mock_exception = {'code': -1,'msg': 'error message'}

key = random_str()
secret = random_str()

orderListId= '1234567'

@mock_http_response(responses.POST, '/api/v3/userDataStream', mock_item, 200)
def test_new_listen_key():
    """ Tests the API endpoint to create a new listen key """

    client =  binance.Stream(key)
    response = client.new_listen_key()
    response.should.equal(mock_item)
