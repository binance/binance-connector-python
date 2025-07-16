# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_algo.algo import Algo
from binance_algo.rest_api.models import QueryHistoricalAlgoOrdersSpotAlgoResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Algo(config_rest_api=configuration)

try:
    response = client.rest_api.query_historical_algo_orders_spot_algo()
    data: QueryHistoricalAlgoOrdersSpotAlgoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
