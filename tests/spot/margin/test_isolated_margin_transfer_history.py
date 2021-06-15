import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": 'Parameter "orderId" was empty.'}

key = random_str()
secret = random_str()

param = {
    "symbol": "BTCUSDT",
    "asset": "BTC",
    "transFrom": "SPOT",
    "transTo": "ISOLATED_MARGIN",
}


def test_isolated_margin_transfer_history_without_symbol():
    """Tests the API endpoint to transfer isolated margin history without asset"""

    client = Client(key, secret)
    client.isolated_margin_transfer_history.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/margin/isolated/transfer\\?" + urlencode(param),
    mock_item,
    200,
)
def test_isolated_margin_transfer_history():
    """Tests the API endpoint to transfer isolated margin history"""

    client = Client(key, secret)
    response = client.isolated_margin_transfer_history(**param)
    response.should.equal(mock_item)
