import asyncio
import os
import logging

from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_PROD_URL,
    ConfigurationWebSocketStreams,
)


from binance_sdk_derivatives_trading_coin_futures.websocket_streams.models import (
    MarkPriceKlineCandlestickStreamsIntervalEnum,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket Streams
configuration_ws_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv(
        "STREAM_URL", DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_PROD_URL
    )
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_ws_streams=configuration_ws_streams)


async def mark_price_kline_candlestick_streams():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.mark_price_kline_candlestick_streams(
            symbol="btcusdt",
            interval=MarkPriceKlineCandlestickStreamsIntervalEnum[""].value,
        )
        stream.on("message", lambda data: print(f"{data}"))

        await asyncio.sleep(5)
        await stream.unsubscribe()
    except Exception as e:
        logging.error(f"mark_price_kline_candlestick_streams() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(mark_price_kline_candlestick_streams())
