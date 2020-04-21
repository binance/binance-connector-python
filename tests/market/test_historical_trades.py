import sure
import binance
import responses

from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}

def test_historical_trades_without_symbol():
    """ Tests the API endpoint to get old trades without symbol """

    api =  binance.API()
    api.historical_trades.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/historicalTrades\\?symbol=BTCUSDT&limit=500', mock_item, 200)
def test_historical_trades_with_default_limit():
    """ Tests the API endpoint to get old trades by default limit """

    api =  binance.API()
    response = api.historical_trades('BTCUSDT')
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/historicalTrades\\?symbol=BTCUSDT&limit=1000', mock_item, 200)
def test_historical_trades_with_limit_1000():
    """ Tests the API endpoint to get recent trades with given limit """

    api =  binance.API()
    response = api.historical_trades('BTCUSDT', limit=1000)

@mock_http_response(responses.GET, '/api/v3/historicalTrades\\?symbol=BTCUSDT&limit=500&fromId=123456789', mock_item, 200)
def test_historical_trades_with_formId():
    """ Tests the API endpoint to get recent trades with given limit """

    api =  binance.API()
    response = api.historical_trades('BTCUSDT', fromId='123456789')
    response.json().should.equal(mock_item)
