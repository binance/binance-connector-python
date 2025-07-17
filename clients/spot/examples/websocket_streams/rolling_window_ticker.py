import asyncio
import os
import logging

from binance_sdk_spot.spot import (
    Spot,
    SPOT_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)
from binance_sdk_spot.websocket_streams.models import RollingWindowTickerWindowSizeEnum

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", SPOT_WS_STREAMS_PROD_URL)
)

# Initialize Spot client
client = Spot(config_ws_streams=configuration_ws_streams)


async def rolling_window_ticker():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.rolling_window_ticker(
            symbol="bnbusdt",
            window_size=RollingWindowTickerWindowSizeEnum["WINDOW_SIZE_1h"].value,
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"rolling_window_ticker() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(rolling_window_ticker())
