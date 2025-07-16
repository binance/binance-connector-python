# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_pay.pay import Pay
from binance_pay.rest_api.models import GetPayTradeHistoryResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Pay(config_rest_api=configuration)

try:
    response = client.rest_api.get_pay_trade_history()
    data: GetPayTradeHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
