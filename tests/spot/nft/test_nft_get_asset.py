import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.lib.utils import encoded_string

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
client = Client(key, secret)

params = {"limit": 50, "page": 1}


@mock_http_response(
    responses.GET,
    "/sapi/v1/nft/user/getAsset",
    mock_item,
    200,
)
def test_nft_asset_without_params():
    """Tests the API endpoint to get NFT Asset info without params"""
    client.nft_asset().should.equal(mock_item)


@mock_http_response(
    responses.GET,
    "/sapi/v1/nft/user/getAsset\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_nft_asset():
    """Tests the API endpoint to get NFT Asset info"""

    client.nft_asset(**params).should.equal(mock_item)
