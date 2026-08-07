# Timeout

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_web3_wallet.web3_wallet import Web3Wallet
from binance_sdk_web3_wallet.rest_api.models import GetPriceInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    timeout=2000
)
client = Web3Wallet(config_rest_api=configuration_rest_api)

try:
    response = client.rest_api.get_price_info()
    data: GetPriceInfoResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
