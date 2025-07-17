# Compression Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_options.derivatives_trading_options import DerivativesTradingOptions
from binance_sdk_derivatives_trading_options.rest_api.models import OptionAccountInformationResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=False
)
client = DerivativesTradingOptions(config_rest_api=configuration)

try:
    response = client.rest_api.option_account_information()
    data: OptionAccountInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
