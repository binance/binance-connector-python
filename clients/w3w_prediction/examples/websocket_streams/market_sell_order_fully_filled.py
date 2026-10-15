import asyncio
import os
import logging

from binance_sdk_w3w_prediction.w3w_prediction import (
    W3wPrediction,
    W3W_PREDICTION_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    stream_url=os.getenv("STREAM_URL", W3W_PREDICTION_WS_STREAMS_PROD_URL),
)

# Initialize W3wPrediction client
client = W3wPrediction(config_ws_streams=configuration_ws_streams)


async def market_sell_order_fully_filled():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.market_sell_order_fully_filled()
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"market_sell_order_fully_filled() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(market_sell_order_fully_filled())
