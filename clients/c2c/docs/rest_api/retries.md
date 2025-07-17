# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_c2c.c2c import C2C
from binance_sdk_c2c.rest_api.models import GetC2CTradeHistoryResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
)
client = C2C(config_rest_api=configuration)

try:
    response = client.rest_api.get_c2_c_trade_history()
    data: GetC2CTradeHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
