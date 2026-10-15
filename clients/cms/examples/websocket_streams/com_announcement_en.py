import asyncio
import os
import logging

from binance_sdk_cms.cms import (
    Cms,
    CMS_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", CMS_WS_STREAMS_PROD_URL)
)
configuration_ws_streams.api_key = os.getenv("API_KEY", "")
configuration_ws_streams.api_secret = os.getenv("API_SECRET", "")

# Initialize Cms client
client = Cms(config_ws_streams=configuration_ws_streams)


async def com_announcement_en():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.com_announcement_en()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"com_announcement_en() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(com_announcement_en())
