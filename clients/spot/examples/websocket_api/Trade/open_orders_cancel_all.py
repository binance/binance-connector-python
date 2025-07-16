import asyncio
import os
import logging

from binance_spot.spot import Spot, SPOT_WS_API_PROD_URL, ConfigurationWebSocketAPI


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket API
configuration_ws_api = ConfigurationWebSocketAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    stream_url=os.getenv("STREAM_URL", SPOT_WS_API_PROD_URL),
)

# Initialize Spot client
client = Spot(config_ws_api=configuration_ws_api)


async def open_orders_cancel_all():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.open_orders_cancel_all(
            symbol="BNBUSDT",
        )

        rate_limits = response.rate_limits
        logging.info(f"open_orders_cancel_all() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"open_orders_cancel_all() response: {data}")
    except Exception as e:
        logging.error(f"open_orders_cancel_all() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(open_orders_cancel_all())
