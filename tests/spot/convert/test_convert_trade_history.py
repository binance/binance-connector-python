import responses
from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from tests.util import current_timestamp
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


params = {
    "startTime": current_timestamp(),
    "endTime": current_timestamp(),
}

client = Client(key, secret)


def test_convert_trade_history_without_startTime():
    """Tests the API endpoint to retrieve convert trade history without startTime"""

    client.convert_trade_history.when.called_with(
        startTime="", endTime=1597130241000
    ).should.throw(ParameterRequiredError)


def test_convert_trade_history_without_endTime():
    """Tests the API endpoint to retrieve convert trade history without endTime"""

    client.convert_trade_history.when.called_with(
        startTime=1597130241000, endTime=""
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/convert/tradeFlow\\?" + urlencode(params), mock_item, 200
)
def test_convert_trade_history():
    """Tests the API endpoint to retrieve convert trade history"""

    response = client.convert_trade_history(**params)
    response.should.equal(mock_item)
