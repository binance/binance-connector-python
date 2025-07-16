# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import DerivativesTradingPortfolioMargin
from binance_derivatives_trading_portfolio_margin.rest_api.models import AccountInformationResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = DerivativesTradingPortfolioMargin(config_rest_api=configuration)

try:
    response = client.rest_api.account_information()
    data: AccountInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
