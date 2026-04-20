import asyncio
import os
import logging

from binance_sdk_spot.spot import Spot, SPOT_WS_API_PROD_URL, ConfigurationWebSocketAPI

from binance_sdk_spot.websocket_api.models import OrderListPlaceOpoWorkingTypeEnum
from binance_sdk_spot.websocket_api.models import OrderListPlaceOpoWorkingSideEnum
from binance_sdk_spot.websocket_api.models import OrderListPlaceOpoPendingTypeEnum
from binance_sdk_spot.websocket_api.models import OrderListPlaceOpoPendingSideEnum

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


async def order_list_place_opo():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.order_list_place_opo(
            symbol="BNBUSDT",
            working_type=OrderListPlaceOpoWorkingTypeEnum["LIMIT"].value,
            working_side=OrderListPlaceOpoWorkingSideEnum["BUY"].value,
            working_price=1.0,
            working_quantity=1.0,
            pending_type=OrderListPlaceOpoPendingTypeEnum["LIMIT"].value,
            pending_side=OrderListPlaceOpoPendingSideEnum["BUY"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_list_place_opo() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_list_place_opo() response: {data}")

    except Exception as e:
        logging.error(f"order_list_place_opo() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(order_list_place_opo())
