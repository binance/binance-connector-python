import sure
import binance
import responses

from tests.util import mock_http_response
from binance.error import ParameterRequiredError


mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

@mock_http_response(responses.GET, '/api/v3/time', mock_item, 200)
def test_time():
    """ Tests the API endpoint to get exchange time """

    api =  binance.API()
    response = api.time()
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/exchangeInfo', mock_item, 200)
def test_exchange_info():
    """ Tests the API endpoint to get exchange info """

    api =  binance.API()
    response = api.exchange_info()
    response.json().should.equal(mock_item)

def test_depth_without_symbol():
    """ Tests the API endpoint to get exchange order book depth without symbol"""

    api =  binance.API()
    api.depth.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/depth\\?symbol=BTCUSDT&limit=100', mock_item, 200)
def test_depth():
    """ Tests the API endpoint to get exchange order book depth with default limit 100 """

    api =  binance.API()
    response = api.depth('BTCUSDT')
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/depth\\?symbol=BTCUSDT&limit=10', mock_item, 200)
def test_depth_fixed_limit():
    """ Tests the API endpoint to get exchange order book depth with limit 10 """

    api =  binance.API()
    response = api.depth('BTCUSDT', limit=10)
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/trades\\?symbol=BTCUSDT&limit=500', mock_item, 200)
def test_trades_with_default_limit():
    """ Tests the API endpoint to get recent trades with default limit """

    api =  binance.API()
    response = api.trades('BTCUSDT')
    response.json().should.equal(mock_item)
