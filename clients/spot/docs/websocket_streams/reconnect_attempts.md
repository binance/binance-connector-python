# Reconnect Attempts

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import TimeUnit
from binance_sdk_spot.spot import Spot

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    reconnect_attempts=3,
)

client = Spot(config_ws_streams=configuration_ws_streams)


async def agg_trade():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        connection.on_connection("open", lambda: print("OPEN MESSAGE"))
        connection.on_connection("ping", lambda: print("PING MESSAGE"))
        connection.on_connection("pong", lambda: print("PONG MESSAGE"))
        connection.on_connection("error", lambda data: print(f"ERROR MESSAGE: {data}"))
        connection.on_connection("close", lambda: print("CLOSE MESSAGE"))

        stream = await connection.agg_trade(
            symbol="bnbusdt",
        )
        stream.on("message", lambda data: print(f"DATA: {data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"agg_trade() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(agg_trade())
```
