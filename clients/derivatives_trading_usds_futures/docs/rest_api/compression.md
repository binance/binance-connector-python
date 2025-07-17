# Compression Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import DerivativesTradingUsdsFutures
from binance_sdk_derivatives_trading_usds_futures.rest_api.models import ExchangeInformationResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=False
)
client = DerivativesTradingUsdsFutures(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_information()
    data: ExchangeInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
