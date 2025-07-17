# Timeout

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_nft.nft import NFT
from binance_sdk_nft.rest_api.models import AcquiringAlgorithmResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
)
client =  NFT(config_rest_api=configuration)

try:
    response = client.rest_api.get_nft_asset()
    data: AcquiringAlgorithmResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
