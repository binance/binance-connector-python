# Connection Mode

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import WebsocketMode
from binance_sdk_alpha.alpha import Alpha

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(mode=WebsocketMode.POOL, pool_size=3)

client = Alpha(config_ws_streams=configuration_ws_streams)


async def connect:
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        await asyncio.sleep(5)
    except Exception as e:
        logging.error(f"connect error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(connect)
```
