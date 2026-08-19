# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_stocks.stocks import Stocks
from binance_sdk_stocks.rest_api.models import ExchangeInfoResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Stocks(config_rest_api=configuration_rest_api)

try:
    response = client.rest_api.exchange_info()
    data: ExchangeInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
