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

client = Client(key, secret)

parameterized_test_data = [
    ({"startTime": None, "endTime": endTime}),
    ({"startTime": startTime, "endTime": None}),
]


@pytest.mark.parametrize("params", parameterized_test_data)
def test_convert_history_with_missing_field(params):
    """Tests the API endpoint to get busd convert history with missing parameter"""
    client.convert_history.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


params = {"startTime": startTime, "endTime": endTime}


@mock_http_response(
    responses.GET,
    "/sapi/v1/asset/convert-transfer/queryByPage\\?" + urlencode(params),
    mock_item,
    200,
)
def test_convert_history():
    """Tests the API endpoint to get busd convert history"""

    client = Client(key, secret)
    response = client.convert_history(**params)
    response.should.equal(mock_item)
