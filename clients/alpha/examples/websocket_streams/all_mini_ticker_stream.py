import asyncio
import os
import logging

from binance_sdk_alpha.alpha import (
    Alpha,
    ALPHA_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", ALPHA_WS_STREAMS_PROD_URL)
)

# Initialize Alpha client
client = Alpha(config_ws_streams=configuration_ws_streams)


async def all_mini_ticker_stream():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.all_mini_ticker_stream()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"all_mini_ticker_stream() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(all_mini_ticker_stream())
