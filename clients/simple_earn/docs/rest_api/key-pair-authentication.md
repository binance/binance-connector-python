# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_simple_earn.simple_earn import SimpleEarn
from binance_simple_earn.rest_api.models import GetSimpleEarnLockedProductListResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = SimpleEarn(config_rest_api=configuration)

try:
    response = client.rest_api.get_simple_earn_flexible_product_list()
    data: GetSimpleEarnLockedProductListResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
