# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_wallet.wallet import Wallet
from binance_sdk_wallet.rest_api.models import AccountInfoResponse

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
client = Wallet(config_rest_api=configuration)

try:
    response = client.rest_api.account_info()
    data: AccountInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
