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
type = 1

params = {"asset": asset, "amount": amount, "type": type}


def test_margin_transfer_without_asset():
    """Tests the API endpoint to margin tranfer without asset"""

    client = Client(key, secret)
    client.margin_transfer.when.called_with("", amount, type).should.throw(
        ParameterRequiredError
    )


def test_margin_transfer_without_amount():
    """Tests the API endpoint to margin tranfer without amount"""

    client = Client(key, secret)
    client.margin_transfer.when.called_with("", amount, type).should.throw(
        ParameterRequiredError
    )


def test_margin_transfer_without_type():
    """Tests the API endpoint to margin tranfer without type"""

    client = Client(key, secret)
    client.margin_transfer.when.called_with("", amount, type).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/margin/transfer\\?" + urlencode(params), mock_item, 200
)
def test_margin_transfer():
    """Tests the API endpoint to margin tranfer"""

    client = Client(key, secret)
    response = client.margin_transfer(**params)
    response.should.equal(mock_item)
