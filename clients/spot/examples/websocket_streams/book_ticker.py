import asyncio
import os
import logging

from binance_sdk_spot.spot import (
    Spot,
    SPOT_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", SPOT_WS_STREAMS_PROD_URL)
)

# Initialize Spot client
client = Spot(config_ws_streams=configuration_ws_streams)


async def book_ticker():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.book_ticker(
            symbol="bnbusdt",
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"book_ticker() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(book_ticker())
