import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_sub_account_futures_asset_transfer_history_without_email():
    """Tests the API endpoint to  query sub account futures asset transfer history without email"""

    param = {"email": "", "futuresType": 1}
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer_history.when.called_with(
        **param
    ).should.throw(ParameterRequiredError)


def test_sub_account_futures_asset_transfer_history_without_futurestype():
    """Tests the API endpoint to  query sub account futures asset transfer history without email"""

    param = {"email": "alice@test.com", "futuresType": ""}
    client = Client(key, secret)
    client.sub_account_futures_asset_transfer_history.when.called_with(
        **param
    ).should.throw(ParameterRequiredError)


@mock_http_response(
    responses.GET,
    "/sapi/v1/sub-account/futures/internalTransfer\\?email=alice@test.com&futuresType=1",
    mock_item,
    200,
)
def test_sub_account_futures_asset_transfer_history():
    """Tests the API endpoint to query sub account futures asset transfer history"""

    params = {"email": "alice@test.com", "futuresType": 1}
    client = Client(key, secret)
    response = client.sub_account_futures_asset_transfer_history(**params)
    response.should.equal(mock_item)
