# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_sub_account.sub_account import SubAccount
from binance_sdk_sub_account.rest_api.models import GetSummaryOfSubAccountsMarginAccountResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = SubAccount(config_rest_api=configuration)

try:
    response = client.rest_api.get_summary_of_sub_accounts_margin_account()
    data: GetSummaryOfSubAccountsMarginAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
