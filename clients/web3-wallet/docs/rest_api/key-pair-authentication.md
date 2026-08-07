# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_web3_wallet.web3_wallet import Web3Wallet
from binance_sdk_web3_wallet.rest_api.models import GetPriceInfoResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Web3Wallet(config_rest_api=configuration_rest_api)

try:
    response = client.rest_api.get_price_info()
    data: GetPriceInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
