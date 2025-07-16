# Keep-Alive Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_rebate.rebate import Rebate
from binance_rebate.rest_api.models import GetSpotRebateHistoryRecordsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    keep_alive=False
)
client = Rebate(config_rest_api=configuration)

try:
    response = client.rest_api.get_spot_rebate_history_records()
    data: GetSpotRebateHistoryRecordsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
