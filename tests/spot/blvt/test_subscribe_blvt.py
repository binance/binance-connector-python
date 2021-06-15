import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_subscribe_blvt_without_tokenName():
    """Tests the API endpoint to subscribe BLVT without tokenName"""

    client = Client(key, secret)
    client.subscribe_blvt.when.called_with("", "10").should.throw(
        ParameterRequiredError
    )


def test_subscribe_blvt_without_cost():
    """Tests the API endpoint to subscribe BLVT without cost"""

    client = Client(key, secret)
    client.subscribe_blvt.when.called_with("BTCUP", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/blvt/subscribe\\?tokenName=BTCUP&cost=10", mock_item, 200
)
def test_subscribe_blvt():
    """Tests the API endpoint to subscribe BLVT"""

    client = Client(key, secret)
    response = client.subscribe_blvt("BTCUP", "10")
    response.should.equal(mock_item)
