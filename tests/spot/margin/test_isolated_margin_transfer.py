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
    "asset": "BTC",
    "symbol": "BTCUSDT",
    "transFrom": "SPOT",
    "transTo": "ISOLATED_MARGIN",
    "amount": "1",
}


def test_isolated_margin_transfer_without_asset():
    """Tests the API endpoint to transfer isolated margin without asset"""

    params = {
        "asset": "",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    client.isolated_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_isolated_margin_transfer_without_symbol():
    """Tests the API endpoint to transfer isolated margin without symbol"""

    params = {
        "asset": "USDT",
        "symbol": "",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    client.isolated_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_isolated_margin_transfer_without_transForm():
    """Tests the API endpoint to transfer isolated margin without transForm"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "",
        "transTo": "ISOLATED_MARGIN",
        "amount": "1",
    }
    client = Client(key, secret)
    client.isolated_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_isolated_margin_transfer_without_transTo():
    """Tests the API endpoint to transfer isolated margin without transTo"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "",
        "amount": "1",
    }
    client = Client(key, secret)
    client.isolated_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_isolated_margin_transfer_without_amount():
    """Tests the API endpoint to transfer isolated margin without amount"""

    params = {
        "asset": "USDT",
        "symbol": "BTCUSDT",
        "transFrom": "SPOT",
        "transTo": "ISOLATED_MARGIN",
        "amount": "",
    }
    client = Client(key, secret)
    client.isolated_margin_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/isolated/transfer\\?" + urlencode(param),
    mock_item,
    200,
)
def test_isolated_margin_transfer():
    """Tests the API endpoint to transfer isolated margin"""

    client = Client(key, secret)
    response = client.isolated_margin_transfer(**param)
    response.should.equal(mock_item)
