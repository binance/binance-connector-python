# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_c2c.c2c import C2C
from binance_sdk_c2c.rest_api.models import GetC2CTradeHistoryResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = C2C(config_rest_api=configuration)

try:
    response = client.rest_api.get_c2_c_trade_history()
    data: GetC2CTradeHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
