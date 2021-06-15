import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_bswap_swap_without_quoteAsset():
    """Swap quoteAsset for baseAsset without quoteAsset"""

    client = Client(key, secret)
    client.bswap_swap.when.called_with("", "BUSD", "30000").should.throw(
        ParameterRequiredError
    )


def test_bswap_swap_without_baseAsset():
    """Swap quoteAsset for baseAsset without baseAsset"""

    client = Client(key, secret)
    client.bswap_swap.when.called_with("USDT", "", "30000").should.throw(
        ParameterRequiredError
    )


def test_bswap_swap_without_quoteQty():
    """Swap quoteAsset for baseAsset without quoteQty"""

    client = Client(key, secret)
    client.bswap_swap.when.called_with("USDT", "BUSD", None).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/bswap/swap\\?quoteAsset=USDT&baseAsset=BUSD&quoteQty=30000",
    mock_item,
    200,
)
def test_bswap_swap():
    """Swap quoteAsset for baseAsset."""

    client = Client(key, secret)
    response = client.bswap_swap("USDT", "BUSD", "30000")
    response.should.equal(mock_item)
