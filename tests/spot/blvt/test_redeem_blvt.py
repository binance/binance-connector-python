import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_redeem_blvt_without_tokenName():
    """Tests the API endpoint to Redeem BLVT without tokenName"""

    client = Client(key, secret)
    client.redeem_blvt.when.called_with("", "1").should.throw(ParameterRequiredError)


def test_redeem_blvt_without_amount():
    """Tests the API endpoint to Redeem BLVT without amount"""

    client = Client(key, secret)
    client.redeem_blvt.when.called_with("BTCUP", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST, "/sapi/v1/blvt/redeem\\?tokenName=BTCUP&amount=1", mock_item, 200
)
def test_redeem_blvt():
    """Tests the API endpoint to Redeem BLVT"""

    client = Client(key, secret)
    response = client.redeem_blvt("BTCUP", "1")
    response.should.equal(mock_item)
