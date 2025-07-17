# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import DerivativesTradingUsdsFutures
from binance_sdk_derivatives_trading_usds_futures.rest_api.models import ExchangeInformationResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = DerivativesTradingUsdsFutures(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_information()
    data: ExchangeInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
