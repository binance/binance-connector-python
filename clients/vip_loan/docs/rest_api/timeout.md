# Timeout

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_vip_loan.vip_loan import VipLoan
from binance_sdk_vip_loan.rest_api.models import GetCollateralAssetDataResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
)
client =  VipLoan(config_rest_api=configuration)

try:
    response = client.rest_api.get_collateral_asset_data()
    data: GetCollateralAssetDataResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
