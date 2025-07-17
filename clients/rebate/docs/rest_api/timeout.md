# Timeout

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_rebate.rebate import Rebate
from binance_sdk_rebate.rest_api.models import GetSpotRebateHistoryRecordsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
)
client =  Rebate(config_rest_api=configuration)

try:
    response = client.rest_api.get_spot_rebate_history_records()
    data: GetSpotRebateHistoryRecordsResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
