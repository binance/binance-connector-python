# Proxy

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.websocket_api.models import exchange_info_response_result

configuration_ws_api = ConfigurationWebSocketAPI(
    proxy={
        "host": "localhost",
        "port": 8080,
        "protocol": "http",  # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    }
)

client = Spot(config_ws_api=configuration_ws_api)

async def exchange_info():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await client.websocket_api.exchange_info(
            symbol="BNBUSDT",
        )

        rate_limits = response.rate_limits
        logging.info(f"exchange_info() rate limits: {rate_limits}")

        data: exchange_info_response_result = response.data()
        logging.info(f"exchange_info() response: {data}")
    except Exception as e:
        logging.error(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

if __name__ == "__main__":
    asyncio.run(exchange_info())
```
