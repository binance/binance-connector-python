# HTTPS Agent Configuration

```python
import ssl

from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_w3w_prediction.w3w_prediction import W3wPrediction
from binance_sdk_w3w_prediction.rest_api.models import ListPredictionCategoriesResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = W3wPrediction(config_rest_api=configuration)

try:
    response = client.rest_api.list_prediction_categories()
    data: ListPredictionCategoriesResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
