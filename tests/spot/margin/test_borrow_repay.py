import responses

from urllib.parse import urlencode
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

asset = "BNB"
amount = "100"
isIsolated = "TRUE"
symbol = "BNBUSDT"
type = "BORROW"

params = {
    "asset": asset,
    "amount": amount,
    "type": type,
    "isIsolated": isIsolated,
    "symbol": symbol,
}


def test_borrow_repay_without_asset():
    """Tests the API endpoint to margin borrow without asset"""

    client = Client(key, secret)
    client.borrow_repay.when.called_with(
        "", isIsolated, symbol, amount, type
    ).should.throw(ParameterRequiredError)


def test_borrow_repay_without_isIsolated():
    """Tests the API endpoint to margin borrow isIsolated"""

    client = Client(key, secret)
    client.borrow_repay.when.called_with(asset, "", symbol, amount, type).should.throw(
        ParameterRequiredError
    )


def test_borrow_repay_without_symbol():
    """Tests the API endpoint to margin borrow symbol"""

    client = Client(key, secret)
    client.borrow_repay.when.called_with(
        asset, isIsolated, "", amount, type
    ).should.throw(ParameterRequiredError)


def test_borrow_repay_without_amount():
    """Tests the API endpoint to margin borrow without amount"""

    client = Client(key, secret)
    client.borrow_repay.when.called_with(
        asset, isIsolated, symbol, "", type
    ).should.throw(ParameterRequiredError)


def test_borrow_repay_without_type():
    """Tests the API endpoint to margin borrow without type"""

    client = Client(key, secret)
    client.borrow_repay.when.called_with(
        asset, isIsolated, symbol, amount, ""
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/borrow-repay\\?" + urlencode(params),
    mock_item,
    200,
)
def test_borrow_repay():
    """Tests the API endpoint to margin borrow"""

    client = Client(key, secret)
    response = client.borrow_repay(**params)
    response.should.equal(mock_item)
