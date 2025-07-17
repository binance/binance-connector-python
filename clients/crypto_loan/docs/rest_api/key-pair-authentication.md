# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_crypto_loan.crypto_loan import CryptoLoan
from binance_sdk_crypto_loan.rest_api.models import GetFlexibleLoanBorrowHistoryResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = CryptoLoan(config_rest_api=configuration)

try:
    response = client.rest_api.get_flexible_loan_borrow_history()
    data: GetFlexibleLoanBorrowHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
