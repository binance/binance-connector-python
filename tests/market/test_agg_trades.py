import sure
import binance
import responses

from tests.util import mock_http_response
from tests.util import random_id
from tests.util import timestamp
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
fromId = random_id()
startTime = timestamp()
endTime = startTime + random_id()

def test_agg_trades_without_symbol():
    """ Tests the API endpoint to get old trades without symbol """

    api =  binance.API()
    api.agg_trades.when.called_with('').should.throw(ParameterRequiredError)

@mock_http_response(responses.GET, '/api/v3/aggTrades\\?symbol=BTCUSDT&limit=500', mock_item, 200)
def test_agg_trades_with_default_limit():
    """ Tests the API endpoint to get agg trades by default limit """

    api =  binance.API()
    response = api.agg_trades('BTCUSDT')
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/aggTrades\\?symbol=BTCUSDT&limit=1000', mock_item, 200)
def test_agg_trades_with_limit_1000():
    """ Tests the API endpoint to get agg trades with given limit """

    api =  binance.API()
    response = api.agg_trades('BTCUSDT', limit=1000)

@mock_http_response(responses.GET, '/api/v3/aggTrades\\?symbol=BTCUSDT&limit=500&fromId=' + str(fromId), mock_item, 200)
def test_agg_trades_with_formId():
    """ Tests the API endpoint to get agg trades with fromId """

    api =  binance.API()
    response = api.agg_trades('BTCUSDT', fromId=fromId)
    response.json().should.equal(mock_item)

@mock_http_response(responses.GET, '/api/v3/aggTrades\\?symbol=BTCUSDT&limit=500&startTime=' + str(startTime) + '&endTime=' + str(endTime), mock_item, 200)
def test_agg_trades_with_timestamp():
    """ Tests the API endpoint to get agg trades with specific timestamp """

    api =  binance.API()
    response = api.agg_trades('BTCUSDT', startTime=startTime, endTime=endTime)
    response.json().should.equal(mock_item)
