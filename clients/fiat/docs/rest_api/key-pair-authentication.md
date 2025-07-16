# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_fiat.fiat import Fiat
from binance_fiat.rest_api.models import GetFiatDepositWithdrawHistoryResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Fiat(config_rest_api=configuration)

try:
    response = client.rest_api.get_fiat_deposit_withdraw_history()
    data: GetFiatDepositWithdrawHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
