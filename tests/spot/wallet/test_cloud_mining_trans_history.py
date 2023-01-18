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
    ({"startTime": None, "endTime": endTime}),
    ({"startTime": startTime, "endTime": None}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_cloud_mining_trans_history_with_missing_field(params):
    """Tests the API endpoint to get cloud-mining payment and refund history with missing field"""
    client = Client(key, secret)
    client.cloud_mining_trans_history.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


params = {"startTime": startTime, "endTime": endTime}


@mock_http_response(
    responses.GET,
    "/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage\\?" + urlencode(params),
    mock_item,
    200,
)
def test_cloud_mining_trans_history():
    """Tests the API endpoint to get cloud-mining payment and refund history"""

    client = Client(key, secret)
    response = client.cloud_mining_trans_history(**params)
    response.should.equal(mock_item)
