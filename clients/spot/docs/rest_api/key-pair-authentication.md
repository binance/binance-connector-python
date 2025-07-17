# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.rest_api.models import GetAccountResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Spot(config_rest_api=configuration)

try:
    response = client.rest_api.get_account()
    data: GetAccountResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
