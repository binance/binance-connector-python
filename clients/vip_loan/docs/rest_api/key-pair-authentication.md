# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_vip_loan.vip_loan import VipLoan
from binance_sdk_vip_loan.rest_api.models import GetCollateralAssetDataResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = VipLoan(config_rest_api=configuration)

try:
    response = client.rest_api.get_collateral_asset_data()
    data: GetCollateralAssetDataResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
