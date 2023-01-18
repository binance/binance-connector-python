import responses
import pytest
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from urllib.parse import urlencode
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

parameterized_test_params = [
    ({"coin": "", "enable": True}),
    ({"coin": "USDC", "enable": None}),
]


@pytest.mark.parametrize("params", parameterized_test_params)
def test_toggle_auto_convertion_with_missing_field(params):
    """Tests the API endpoint to toggle auto convertion with missing field"""

    client = Client(key, secret)
    client.toggle_auto_convertion.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


params = {"coin": "USDC", "enable": True}


@mock_http_response(
    responses.POST,
    "/sapi/v1/capital/contract/convertible-coins\\?" + urlencode(params),
    mock_item,
    200,
)
def test_toggle_auto_convertion():
    """Tests the API endpoint to toggle auto convertion"""

    client = Client(key, secret)
    response = client.toggle_auto_convertion(**params)
    response.should.equal(mock_item)
