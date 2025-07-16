# HTTPS Agent Configuration

```python
import ssl

from binance_common.configuration import ConfigurationRestAPI
from binance_convert.convert import Convert
from binance_convert.rest_api.models import ListAllConvertPairsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = Convert(config_rest_api=configuration)

try:
    response = client.rest_api.list_all_convert_pairs()
    data: ListAllConvertPairsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
