import asyncio
import os
import logging

from binance_sdk_alpha.alpha import (
    Alpha,
    ALPHA_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


from binance_sdk_alpha.websocket_streams.models import KlineStreamIntervalEnum

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", ALPHA_WS_STREAMS_PROD_URL)
)

# Initialize Alpha client
client = Alpha(config_ws_streams=configuration_ws_streams)


async def kline_stream():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.kline_stream(
            symbol="alpha_116usdt",
            interval=KlineStreamIntervalEnum[""].value,
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"kline_stream() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(kline_stream())
