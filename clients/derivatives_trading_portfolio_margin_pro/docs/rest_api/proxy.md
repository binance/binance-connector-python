# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro
from binance_derivatives_trading_portfolio_margin_pro.rest_api.models import GetPortfolioMarginProAccountInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    proxy = {
        "host": "127.0.0.1",
        "port": 8080,
        "protocol": "http", # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    }
)
client = DerivativesTradingPortfolioMarginPro(config_rest_api=configuration)

try:
    response = client.rest_api.get_portfolio_margin_pro_account_info()
    data: GetPortfolioMarginProAccountInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
