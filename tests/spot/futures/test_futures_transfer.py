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

params = {"asset": "BTC", "amount": "1", "type": 1}


def test_futures_transfer_without_asset():
    """Tests the API endpoint to transfer futures funds without asset"""

    params = {"asset": "", "amount": "1", "type": 1}
    client = Client(key, secret)
    client.futures_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_transfer_without_amount():
    """Tests the API endpoint to transfer futures funds without amount"""

    params = {"asset": "BTC", "amount": "", "type": 1}
    client = Client(key, secret)
    client.futures_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_futures_transfer_without_type():
    """Tests the API endpoint to transfer futures funds without type"""

    params = {"asset": "BTC", "amount": "1", "type": ""}
    client = Client(key, secret)
    client.futures_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/futures/transfer\\?" + urlencode(params), mock_item, 200
)
def test_futures_transfer():
    """Tests the API endpoint to transfer futures funds"""

    client = Client(key, secret)
    response = client.futures_transfer(**params)
    response.should.equal(mock_item)
