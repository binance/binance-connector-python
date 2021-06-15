import responses

from binance.lib.utils import encoded_string
from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

params = {
    "email": "alice@test.com",
    "futuresType": 1,  # 1:USDT Margined Futures, 2:COIN Margined Futures
    "recvWindow": 1000,
}


def test_sub_account_futures_account_v2_without_email():
    """Tests the API endpoint to get sub account futures account without email"""

    params = {"email": "", "futuresType": 1, "recvWindow": 1000}

    client = Client(key, secret)
    client.sub_account_futures_account.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_sub_account_futures_account_v2_without_futuresType():
    """Tests the API endpoint to get sub account futures account without futuresType"""

    params = {"email": "alice@test.com", "futuresType": "", "recvWindow": 1000}

    client = Client(key, secret)
    client.sub_account_futures_account.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v2/sub-account/futures/account\\?" + encoded_string(params),
    mock_item,
    200,
)
def test_sub_account_futures_account_v2():
    """Tests the API endpoint to get sub account futures account"""

    client = Client(key, secret)
    response = client.sub_account_futures_account(**params)
    response.should.equal(mock_item)
