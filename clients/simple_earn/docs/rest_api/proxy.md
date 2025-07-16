# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_simple_earn.simple_earn import SimpleEarn
from binance_simple_earn.rest_api.models import GetSimpleEarnLockedProductListResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    proxy = {
        "host": "127.0.0.1",
        "port": 8080,
        "protocol": "http", # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    }
)
client = SimpleEarn(config_rest_api=configuration)

try:
    response = client.rest_api.get_simple_earn_flexible_product_list()
    data: GetSimpleEarnLockedProductListResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
