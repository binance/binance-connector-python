# Retries Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_gift_card.gift_card import GiftCard
from binance_gift_card.rest_api.models import CreateASingleTokenGiftCardResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
    retries=2
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
