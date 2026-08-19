# HTTPS Agent Configuration

```python
import ssl

from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_stocks.stocks import Stocks
from binance_sdk_stocks.rest_api.models import ExchangeInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = Stocks(config_rest_api=configuration_rest_api)

try:
    response = client.rest_api.exchange_info()
    data: ExchangeInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
