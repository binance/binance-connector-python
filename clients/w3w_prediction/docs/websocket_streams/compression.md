# Compression

```python
import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_sdk_w3w_prediction.w3w_prediction import W3wPrediction

logging.basicConfig(level=logging.INFO)

configuration_ws_streams = ConfigurationWebSocketStreams(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=0,
)

client = W3wPrediction(config_ws_streams=configuration_ws_streams)


async def prediction_order_book_all():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.prediction_order_book_all()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"prediction_order_book_all() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(prediction_order_book_all())
```
