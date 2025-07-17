# HTTPS Agent Configuration

```python
import ssl

from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_margin_trading.margin_trading import MarginTrading
from binance_sdk_margin_trading.rest_api.models import GetSummaryOfMarginAccountResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = MarginTrading(config_rest_api=configuration)

try:
    response = client.rest_api.get_summary_of_margin_account()
    data: GetSummaryOfMarginAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
