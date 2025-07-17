# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_algo.algo import Algo
from binance_sdk_algo.rest_api.models import QueryHistoricalAlgoOrdersSpotAlgoResponse

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
client = Algo(config_rest_api=configuration)

try:
    response = client.rest_api.query_historical_algo_orders_spot_algo()
    data: QueryHistoricalAlgoOrdersSpotAlgoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
