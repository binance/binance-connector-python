import responses
import pytest
from tests.util import random_str
from tests.util import mock_http_response
from urllib.parse import urlencode
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

client = Client(key, secret)

parameterized_test_data = [({"baseToken": None})]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_gift_card_token_limit_without_params(params):
    """Tests the API endpoint to get token limit without param"""
    client.gift_card_token_limit.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


params = {"baseToken": "BUSD"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/giftcard/buyCode/token-limit\\?" + urlencode(params),
    mock_item,
    200,
)
def test_gift_card_token_limit():
    """Tests the API endpoint to get token limit"""

    response = client.gift_card_token_limit(**params)
    response.should.equal(mock_item)
