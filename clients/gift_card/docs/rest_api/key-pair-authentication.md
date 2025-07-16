# Key Pair Based Authentication

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_gift_card.gift_card import GiftCard
from binance_gift_card.rest_api.models import CreateASingleTokenGiftCardResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = GiftCard(config_rest_api=configuration)

try:
    response = client.rest_api.(
        token="token_example",
        amount=1.0,
    )
    data: CreateASingleTokenGiftCardResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
