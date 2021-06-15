import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance.spot import Spot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_sub_account_futures_account_summary_v2_without_futuresType():
    """Tests the API endpoint to  get sub account futures account summary without futuresType"""

    params = {"futuresType": "", "recvWindow": 1000}

    client = Client(key, secret)
    client.sub_account_futures_account_summary.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.GET,
    "/sapi/v2/sub-account/futures/accountSummary\\?futuresType=1",
    mock_item,
    200,
)
def test_sub_account_futures_account_summary_v2():
    """Tests the API endpoint to get sub account futures account summary"""

    client = Client(key, secret)
    response = client.sub_account_futures_account_summary(futuresType=1)
    response.should.equal(mock_item)
