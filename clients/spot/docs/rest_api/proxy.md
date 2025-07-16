# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_spot.spot import Spot
from binance_spot.rest_api.models import GetAccountResponse

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
client = Spot(config_rest_api=configuration)

try:
    response = client.rest_api.get_account()
    data: GetAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
