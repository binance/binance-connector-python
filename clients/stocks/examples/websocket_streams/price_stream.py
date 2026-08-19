import asyncio
import os
import logging

from binance_sdk_stocks.stocks import (
    Stocks,
    STOCKS_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", STOCKS_WS_STREAMS_PROD_URL)
)

# Initialize Stocks client
client = Stocks(config_ws_streams=configuration_ws_streams)


async def price_stream():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.price_stream()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"price_stream() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(price_stream())
