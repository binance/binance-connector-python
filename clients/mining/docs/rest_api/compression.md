# Compression Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_mining.mining import Mining
from binance_mining.rest_api.models import AcquiringAlgorithmResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=False
)
client = Mining(config_rest_api=configuration)

try:
    response = client.rest_api.acquiring_algorithm()
    data: AcquiringAlgorithmResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
