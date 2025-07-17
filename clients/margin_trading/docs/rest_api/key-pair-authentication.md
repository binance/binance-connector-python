# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_margin_trading.margin_trading import MarginTrading
from binance_sdk_margin_trading.rest_api.models import GetSummaryOfMarginAccountResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = MarginTrading(config_rest_api=configuration)

try:
    response = client.rest_api.get_summary_of_margin_account()
    data: GetSummaryOfMarginAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
