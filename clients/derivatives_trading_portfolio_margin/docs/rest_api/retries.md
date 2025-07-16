# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import DerivativesTradingPortfolioMargin
from binance_derivatives_trading_portfolio_margin.rest_api.models import AccountInformationResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
)
client = DerivativesTradingPortfolioMargin(config_rest_api=configuration)

try:
    response = client.rest_api.account_information()
    data: AccountInformationResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
