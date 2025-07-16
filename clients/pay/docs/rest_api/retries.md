# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_pay.pay import Pay
from binance_pay.rest_api.models import GetPayTradeHistoryResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
)
client = Pay(config_rest_api=configuration)

try:
    response = client.rest_api.get_pay_trade_history()
    data: GetPayTradeHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
