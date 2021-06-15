import responses

from binance.error import ParameterRequiredError, ParameterValueError
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_user_universal_transfer_with_missing_field():
    """Tests the API endpoint to query universal transfer history with missing field"""

    client = Client(key, secret)
    client.user_universal_transfer_history.when.called_with("").should.throw(
        ParameterRequiredError
    )


def test_user_universal_transfer_with_invalid_enum_string():
    """Tests the API endpoint to query universal transfer history with invalid string"""

    client = Client(key, secret)
    client.user_universal_transfer_history.when.called_with(random_str()).should.throw(
        ParameterValueError
    )


@mock_http_response(
    responses.GET, "/sapi/v1/asset/transfer\\?type=UMFUTURE_MAIN", mock_item, 200
)
def test_user_universal_transfer():
    """Tests the API endpoint to query universal transfer history"""

    client = Client(key, secret)
    response = client.user_universal_transfer_history("UMFUTURE_MAIN")
    response.should.equal(mock_item)
