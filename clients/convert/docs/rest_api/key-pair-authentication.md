# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_convert.convert import Convert
from binance_convert.rest_api.models import ListAllConvertPairsResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Convert(config_rest_api=configuration)

try:
    response = client.rest_api.list_all_convert_pairs()
    data: ListAllConvertPairsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
