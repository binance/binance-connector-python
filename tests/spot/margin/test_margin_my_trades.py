import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "symbol": "BNBUSDT",
    "fromId": "from_id",
    "startTime": "1590969041003",
    "endTime": "1590969041003",
    "limit": 10,
    "recvWindow": 1000,
}


@mock_http_response(responses.GET, "/sapi/v1/margin/myTrades", mock_exception, 400)
def test_margin_my_trades_without_asset():
    """Tests the API endpoint to query margin my trades without symbol"""

    client = Client(key, secret)
    client.margin_my_trades.when.called_with("").should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET, "/sapi/v1/margin/myTrades\\?" + urlencode(params), mock_item, 200
)
def test_margin_my_trades():
    """Tests the API endpoint to query margin my trades"""

    client = Client(key, secret)
    response = client.margin_my_trades(**params)
    response.should.equal(mock_item)
