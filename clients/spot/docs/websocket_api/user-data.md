# User Data

```python
import asyncio
import os
import logging

from binance_sdk_spot.spot import Spot, SPOT_WS_API_PROD_URL, ConfigurationWebSocketAPI


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket API
configuration_ws_api = ConfigurationWebSocketAPI(
    api_key="YOUR_API_KEY",
    private_key="YOUR_ED25519_PRIVATE_KEY",
    stream_url=SPOT_WS_API_PROD_URL,
)

# Initialize Spot client
client = Spot(config_ws_api=configuration_ws_api)


async def user_data():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        await connection.session_logon()
        res = await connection.user_data_stream_subscribe()
        response = res.response

        rate_limits = response.rate_limits
        logging.info(f"user_data_stream_subscribe() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"user_data_stream_subscribe() response: {data}")

        res.stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(10)

        await res.stream.unsubscribe()
        await connection.session_logout()
    except Exception as e:
        logging.error(f"user_data() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(user_data())
```