import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_savings_purchase_flexible_product_without_productId():
    """Tests the API endpoint to purchase flexible product without productId"""

    client = Client(key, secret)
    client.savings_purchase_flexible_product.when.called_with("", 10).should.throw(
        ParameterRequiredError
    )


def test_savings_purchase_flexible_product_without_amount():
    """Tests the API endpoint to purchase flexible product without amount"""

    client = Client(key, secret)
    client.savings_purchase_flexible_product.when.called_with("1", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/daily/purchase\\?productId=1&amount=10",
    mock_item,
    200,
)
def test_savings_purchase_flexible_product():
    """Tests the API endpoint to purchase flexible product list"""

    client = Client(key, secret)
    response = client.savings_purchase_flexible_product(productId=1, amount=10)
    response.should.equal(mock_item)
