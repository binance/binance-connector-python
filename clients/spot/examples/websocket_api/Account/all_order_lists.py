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


async def all_order_lists():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.all_order_lists()

        rate_limits = response.rate_limits
        logging.info(f"all_order_lists() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"all_order_lists() response: {data}")
    except Exception as e:
        logging.error(f"all_order_lists() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(all_order_lists())
