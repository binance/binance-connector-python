import responses

from binance.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()


def test_new_isolated_margin_listen_key_without_symbol():
    """Tests the API endpoint to create a new isolated margin listen key without symbol"""

    client = Client(key, secret)
    client.new_isolated_margin_listen_key.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/userDataStream/isolated\\?symbol=BTCUSDT", mock_item, 200
)
def test_new_isolated_margin_listen_key():
    """Tests the API endpoint to create a new isolated margin listen key"""

    param = {"symbol": "BTCUSDT"}
    client = Client(key)
    response = client.new_isolated_margin_listen_key(**param)
    response.should.equal(mock_item)
