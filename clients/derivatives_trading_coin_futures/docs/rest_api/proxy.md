# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import DerivativesTradingCoinFutures
from binance_sdk_derivatives_trading_coin_futures.rest_api.models import ExchangeInformationResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    proxy = {
        "host": "127.0.0.1",
        "port": 8080,
        "protocol": "http", # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    }
)
client = DerivativesTradingCoinFutures(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_information()
    data: ExchangeInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
