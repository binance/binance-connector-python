import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError


mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


def test_bswap_liquidity_remove_without_poolId():
    """Tests the API endpoint to remove liquidity from a pool without poolId."""

    client = Client(key, secret)
    client.bswap_liquidity_remove.when.called_with(
        "", "SINGLE", ["BUSD"], "12415"
    ).should.throw(ParameterRequiredError)


def test_bswap_liquidity_remove_without_type():
    """Tests the API endpoint to remove liquidity from a pool without type."""

    client = Client(key, secret)
    client.bswap_liquidity_remove.when.called_with(
        "2", "", ["BUSD"], "12415"
    ).should.throw(ParameterRequiredError)


def test_bswap_liquidity_remove_without_asset():
    """Tests the API endpoint to remove liquidity from a pool without asset ."""

    client = Client(key, secret)
    client.bswap_liquidity_remove.when.called_with(
        "2", "SINGLE", None, "12415"
    ).should.throw(ParameterRequiredError)


def test_bswap_liquidity_remove_without_shareAmount():
    """Tests the API endpoint to remove liquidity from a pool without shareAmount."""

    client = Client(key, secret)
    client.bswap_liquidity_remove.when.called_with(
        "2", "SINGLE", ["BUSD"], ""
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.POST,
    "/sapi/v1/bswap/liquidityRemove\\?poolId=2&type=SINGLE&asset=BUSD&shareAmount=12415",
    mock_item,
    200,
)
def test_bswap_liquidity_remove():
    """Tests the API endpoint to remove liquidity from a pool"""

    client = Client(key, secret)
    response = client.bswap_liquidity_remove("2", "SINGLE", ["BUSD"], "12415")
    response.should.equal(mock_item)
