# Agent

```python
import asyncio
import ssl
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_sdk_derivatives_trading_options.derivatives_trading_options import DerivativesTradingOptions

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    https_agent=ssl.create_default_context(),
)

client = DerivativesTradingOptions(config_ws_streams=configuration_ws_streams)


async def connect():
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
