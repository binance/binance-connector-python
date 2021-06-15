import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1105, "msg": "error message."}

key = random_str()
secret = random_str()

params = {"asset": "BTC", "startTime": "1597130241000"}


def test_futures_transfer_history_without_asset():
    """Tests the API endpoint to transfer futures funds without asset"""

    params = {"asset": "", "startTime": "1597130241000"}
    client = Client(key, secret)
    client.futures_transfer_history.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_transfer_history_without_startTime():
    """Tests the API endpoint to transfer futures funds without startTime"""

    params = {"asset": "", "startTime": "1597130241000"}
    client = Client(key, secret)
    client.futures_transfer_history.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/futures/transfer\\?" + urlencode(params), mock_item, 200
)
def test_futures_transfer_history():
    """Tests the API endpoint to get futures transfer funds history"""

    client = Client(key, secret)
    response = client.futures_transfer_history(**params)
    response.should.equal(mock_item)
