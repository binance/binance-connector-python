import asyncio
import os
import logging

from binance_sdk_spot.spot import Spot, SPOT_WS_API_PROD_URL, ConfigurationWebSocketAPI

from binance_sdk_spot.websocket_api.models import (
    OrderCancelReplaceCancelReplaceModeEnum,
)
from binance_sdk_spot.websocket_api.models import OrderCancelReplaceSideEnum
from binance_sdk_spot.websocket_api.models import OrderCancelReplaceTypeEnum

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


async def order_cancel_replace():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.order_cancel_replace(
            symbol="BNBUSDT",
            cancel_replace_mode=OrderCancelReplaceCancelReplaceModeEnum[
                "STOP_ON_FAILURE"
            ].value,
            side=OrderCancelReplaceSideEnum["BUY"].value,
            type=OrderCancelReplaceTypeEnum["MARKET"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"order_cancel_replace() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"order_cancel_replace() response: {data}")

    except Exception as e:
        logging.error(f"order_cancel_replace() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(order_cancel_replace())
