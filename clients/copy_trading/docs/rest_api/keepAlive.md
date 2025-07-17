# Keep-Alive Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_copy_trading.copy_trading import CopyTrading
from binance_sdk_copy_trading.rest_api.models import GetFuturesLeadTraderStatusResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    keep_alive=False
)
client = CopyTrading(config_rest_api=configuration)

try:
    response = client.rest_api.get_futures_lead_trader_status()
    data: GetFuturesLeadTraderStatusResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
