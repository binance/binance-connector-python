# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_copy_trading.copy_trading import CopyTrading
from binance_sdk_copy_trading.rest_api.models import GetFuturesLeadTraderStatusResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = CopyTrading(config_rest_api=configuration)

try:
    response = client.rest_api.get_futures_lead_trader_status()
    data: GetFuturesLeadTraderStatusResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
