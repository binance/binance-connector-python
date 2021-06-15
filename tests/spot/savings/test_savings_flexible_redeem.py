import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_flexible_redeem_without_productId():
    """Tests the API endpoint to redeem flexible redemption without productId"""

    client = Client(key, secret)
    client.savings_flexible_redeem.when.called_with("", 10, "NORMAL").should.throw(
        ParameterRequiredError
    )


def test_savings_flexible_redeem_without_amount():
    """Tests the API endpoint to redeem flexible redemption without amount"""

    client = Client(key, secret)
    client.savings_flexible_redeem.when.called_with("1", "", "NORMAL").should.throw(
        ParameterRequiredError
    )


def test_savings_flexible_redeem_without_type():
    """Tests the API endpoint to redeem flexible redemption without type"""

    client = Client(key, secret)
    client.savings_flexible_redeem.when.called_with("1", "10", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/daily/redeem\\?productId=1&amount=2&type=NORMAL",
    mock_item,
    200,
)
def test_savings_flexible_redeem():
    """Tests the API endpoint to get flexible redemption quota"""

    client = Client(key, secret)
    response = client.savings_flexible_redeem(productId="1", amount=2, type="NORMAL")
    response.should.equal(mock_item)
