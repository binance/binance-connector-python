# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_dual_investment.dual_investment import DualInvestment
from binance_dual_investment.rest_api.models import GetDualInvestmentPositionsResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = DualInvestment(config_rest_api=configuration)

try:
    response = client.rest_api.get_dual_investment_product_list()
    data: GetDualInvestmentPositionsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
