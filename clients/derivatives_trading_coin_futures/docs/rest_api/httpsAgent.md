# HTTPS Agent Configuration

```python
import ssl

from binance_common.configuration import ConfigurationRestAPI
from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import DerivativesTradingCoinFutures
from binance_derivatives_trading_coin_futures.rest_api.models import ExchangeInformationResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = DerivativesTradingCoinFutures(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_information()
    data: ExchangeInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
