# Keep-Alive Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_convert.convert import Convert
from binance_sdk_convert.rest_api.models import ListAllConvertPairsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    keep_alive=False
)
client = Convert(config_rest_api=configuration)

try:
    response = client.rest_api.list_all_convert_pairs()
    data: ListAllConvertPairsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
