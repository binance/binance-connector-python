import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_bswap_liquidity_add_without_poolId():
    """Tests the API endpoint to add liquidity to a pool without poolId."""

    client = Client(key, secret)
    client.bswap_liquidity_add.when.called_with("", "BUSD", "1").should.throw(
        ParameterRequiredError
    )


def test_bswap_liquidity_add_without_asset():
    """Tests the API endpoint to add liquidity to a pool without asset."""

    client = Client(key, secret)
    client.bswap_liquidity_add.when.called_with("2", "", "1").should.throw(
        ParameterRequiredError
    )


def test_bswap_liquidity_add_without_quantity():
    """Tests the API endpoint to add liquidity to a pool without quantity."""

    client = Client(key, secret)
    client.bswap_liquidity_add.when.called_with("2", "BUSD", "").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/bswap/liquidityAdd\\?poolId=2&asset=BUSD&quantity=1",
    mock_item,
    200,
)
def test_subscribe_blvt():
    """Tests the API endpoint to add liquidity to a pool."""

    client = Client(key, secret)
    response = client.bswap_liquidity_add("2", "BUSD", "1")
    response.should.equal(mock_item)
