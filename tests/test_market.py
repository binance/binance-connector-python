import sure
import binance
import responses

from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}


def test_agg_trades_without_symbol():
    """ Tests the API endpoint to get old trades without symbol """

    api =  binance.API()
    api.historical_trades.when.called_with('').should.throw(ParameterRequiredError)
