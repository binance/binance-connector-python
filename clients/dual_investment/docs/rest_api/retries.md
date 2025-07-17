# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_dual_investment.dual_investment import DualInvestment
from binance_sdk_dual_investment.rest_api.models import GetDualInvestmentPositionsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
)
client = DualInvestment(config_rest_api=configuration)

try:
    response = client.rest_api.get_dual_investment_product_list()
    data: GetDualInvestmentPositionsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
