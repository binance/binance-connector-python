import asyncio
import os
import logging

from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL,
    ConfigurationWebSocketAPI,
)

from binance_derivatives_trading_coin_futures.websocket_api.models import (
    NewOrderSideEnum,
)
from binance_derivatives_trading_coin_futures.websocket_api.models import (
    NewOrderTypeEnum,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket API
configuration_ws_api = ConfigurationWebSocketAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    stream_url=os.getenv(
        "STREAM_URL", DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_ws_api=configuration_ws_api)


async def new_order():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.new_order(
            symbol="symbol_example",
            side=NewOrderSideEnum["BUY"].value,
            type=NewOrderTypeEnum["LIMIT"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"new_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"new_order() response: {data}")
    except Exception as e:
        logging.error(f"new_order() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(new_order())
