# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro
from binance_sdk_derivatives_trading_portfolio_margin_pro.rest_api.models import GetPortfolioMarginProAccountInfoResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = DerivativesTradingPortfolioMarginPro(config_rest_api=configuration)

try:
    response = client.rest_api.get_portfolio_margin_pro_account_info()
    data: GetPortfolioMarginProAccountInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
