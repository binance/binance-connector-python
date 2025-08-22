# Connection Mode

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import WebsocketMode
from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import DerivativesTradingUsdsFutures

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(mode=WebsocketMode.POOL, pool_size=3)

client = DerivativesTradingUsdsFutures(config_ws_streams=configuration_ws_streams)


async def allBookTickersStream():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.allBookTickersStream()
        stream.on("message", lambda data: print(f"{data}"))
        await asyncio.sleep(5)
    except Exception as e:
        logging.error(f"allBookTickersStream() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(allBookTickersStream())
```
