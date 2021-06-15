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

params = {"asset": asset, "amount": amount}


def test_margin_borrow_without_asset():
    """Tests the API endpoint to margin borrow without asset"""

    client = Client(key, secret)
    client.margin_borrow.when.called_with("", amount).should.throw(
        ParameterRequiredError
    )


def test_margin_borrow_without_amount():
    """Tests the API endpoint to margin borrow without amount"""

    client = Client(key, secret)
    client.margin_borrow.when.called_with(asset, "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/margin/loan\\?" + urlencode(params), mock_item, 200
)
def test_margin_borrow():
    """Tests the API endpoint to margin borrow"""

    client = Client(key, secret)
    response = client.margin_borrow(**params)
    response.should.equal(mock_item)
