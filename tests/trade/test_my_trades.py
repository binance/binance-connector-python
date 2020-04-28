import sure
import binance
import responses

from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
key = random_str()
secret = random_str()

fromId = '1234567'
startTime = current_timestamp()
endTime = current_timestamp()

def test_get_my_trades_without_symbol():
    """ Tests the API endpoint to get my trades without symbol """

    client =  binance.Trade(key, secret)
    client.my_trades.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/myTrades\\?symbol=ETHBTC', mock_item, 200)
def test_get_my_trades():
    """ Tests the API endpoint to get my trades """

    client =  binance.Trade(key, secret)
    response = client.my_trades('ETHBTC')
    response.should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/myTrades\\?symbol=ETHBTC&limit=5&startTime={}&endTime={}&fromId={}'.format(startTime, endTime, fromId), mock_item, 200)
def test_get_my_trades_with_parameters():
    """ Tests the API endpoint to get my trades with extra parameters """

    client =  binance.Trade(key, secret)
    response = client.my_trades('ETHBTC', limit=5, startTime=startTime, endTime=endTime, fromId=fromId)
    response.should.equal(mock_item)
