import responses
import pytest

from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError
from binance.lib.utils import encoded_string


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

complete_params = {
    "poolId": 2,
    "type": "SINGLE",
    "quoteAsset": "USDT",
    "quoteQty": 0.01,
}

parameterized_test_params = [
    ({"poolId": None, "type": None, "quoteAsset": None, "quoteQty": None}),
    ({"poolId": "", "type": "SINGLE", "quoteAsset": "USDT", "quoteQty": 0.01}),
    ({"poolId": 2, "type": "", "quoteAsset": "USDT", "quoteQty": 0.01}),
    ({"poolId": 2, "type": "SINGLE", "quoteAsset": "", "quoteQty": 0.01}),
    ({"poolId": 2, "type": "SINGLE", "quoteAsset": "USDT", "quoteQty": ""}),
]

client = Client(key, secret)


@pytest.mark.parametrize("params", parameterized_test_params)
def test_bswap_add_liquidity_preview_with_missing_param(params):
    """Tests the API endpoint to get add liquidity preview with missing param"""

    client.bswap_add_liquidity_preview.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v1/bswap/addLiquidityPreview\\?" + encoded_string(complete_params),
    mock_item,
    200,
)
def test_bswap_add_liquidity_preview():
    """Tests the API endpoint to get add liquidity preview"""

    response = client.bswap_add_liquidity_preview(**complete_params)
    response.should.equal(mock_item)
