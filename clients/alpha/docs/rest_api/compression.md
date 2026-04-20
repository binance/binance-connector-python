# Compression Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_alpha.alpha import Alpha
from binance_sdk_alpha.rest_api.models import GetExchangeInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=False
)
client = Alpha(config_rest_api=configuration)

try:
    response = client.rest_api.get_exchange_info()
    data: GetExchangeInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
