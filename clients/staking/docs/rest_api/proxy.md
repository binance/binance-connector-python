# Proxy Configuration

```python
from binance_common.configuration import ConfigurationRestAPI
from binance_staking.staking import Staking
from binance_staking.rest_api.models import ClaimBoostRewardsResponse

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
client = Staking(config_rest_api=configuration)

try:
    response = client.rest_api.claim_boost_rewards()
    data: ClaimBoostRewardsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
