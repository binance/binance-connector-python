import asyncio
import os
import logging

from binance_sdk_derivatives_trading_options.derivatives_trading_options import (
    DerivativesTradingOptions,
    DERIVATIVES_TRADING_OPTIONS_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", DERIVATIVES_TRADING_OPTIONS_WS_STREAMS_PROD_URL)
)

# Initialize DerivativesTradingOptions client
client = DerivativesTradingOptions(config_ws_streams=configuration_ws_streams)


async def open_interest():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.open_interest(
            underlying_asset="ETH",
            expiration_date="220930",
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"open_interest() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(open_interest())
