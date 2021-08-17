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
    "symbol": "BTCUSDT",
    "orderId": "345",
    "startTime": current_timestamp(),
    "endTime": current_timestamp(),
    "fromId": "1234567",
    "limit": 500,
    "recvWindow": 1000,
}


def test_get_my_trades_without_symbol():
    """Tests the API endpoint to get my trades without symbol"""

    client = Client(key, secret)
    client.my_trades.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(responses.GET, "/api/v3/myTrades\\?symbol=ETHBTC", mock_item, 200)
def test_get_my_trades():
    """Tests the API endpoint to get my trades"""

    client = Client(key, secret)
    response = client.my_trades("ETHBTC")
    response.should.equal(mock_item)


@mock_http_response(
    responses.GET, "/api/v3/myTrades\\?" + urlencode(params), mock_item, 200
)
def test_get_my_trades_with_parameters():
    """Tests the API endpoint to get my trades with extra parameters"""

    client = Client(key, secret)
    response = client.my_trades(**params)
    response.should.equal(mock_item)
