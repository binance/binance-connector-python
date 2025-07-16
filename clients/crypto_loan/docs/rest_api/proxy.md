# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_crypto_loan.crypto_loan import CryptoLoan
from binance_crypto_loan.rest_api.models import GetFlexibleLoanBorrowHistoryResponse

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
client = CryptoLoan(config_rest_api=configuration)

try:
    response = client.rest_api.get_flexible_loan_borrow_history()
    data: GetFlexibleLoanBorrowHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
