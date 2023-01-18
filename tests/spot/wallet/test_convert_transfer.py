import responses
import pytest

from binance.error import ParameterRequiredError
from urllib.parse import urlencode
from tests.util import random_str, timestamp
from tests.util import mock_http_response
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()
startTime = timestamp()
endTime = timestamp()

parameterized_test_data = [
    ({"clientTranId": None, "asset": "USDT", "amount": 1, "targetAsset": "BUSD"}),
    ({"clientTranId": random_str(), "asset": None, "amount": 1, "targetAsset": "BUSD"}),
    (
        {
            "clientTranId": random_str(),
            "asset": "USDT",
            "amount": None,
            "targetAsset": "BUSD",
        }
    ),
    ({"clientTranId": random_str(), "asset": "USDT", "amount": 1, "targetAsset": None}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_cloud_mining_trans_history_with_missing_field(params):
    """Tests the API endpoint to get busd convert history with missing parameter"""
    client = Client(key, secret)
    client.convert_transfer.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


params = {
    "clientTranId": random_str(),
    "asset": "BUSD",
    "amount": 1,
    "targetAsset": "USDT",
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/asset/convert-transfer\\?" + urlencode(params),
    mock_item,
    200,
)
def test_convert_history():
    """Tests the API endpoint to convert BUSD"""

    client = Client(key, secret)
    response = client.convert_transfer(**params)
    response.should.equal(mock_item)
