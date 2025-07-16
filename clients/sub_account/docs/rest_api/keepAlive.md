# Keep-Alive Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sub_account.sub_account import SubAccount
from binance_sub_account.rest_api.models import GetSummaryOfSubAccountsMarginAccountResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    keep_alive=False
)
client = SubAccount(config_rest_api=configuration)

try:
    response = client.rest_api.get_summary_of_sub_accounts_margin_account()
    data: GetSummaryOfSubAccountsMarginAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
