import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_spot.spot import Spot
from binance_spot.websocket_api.models import open_order_lists_status_response


logging.basicConfig(level=logging.INFO)

configuration_ws_api = ConfigurationWebSocketAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)

client = Spot(config_ws_api=configuration_ws_api)


async def exchange_info():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await client.websocket_api.open_order_lists_status()

        rate_limits = response.rate_limits
        logging.info("Rate Limits: ", rate_limits)

        data: open_order_lists_status_response = response.data()
        logging.info(f"exchange_info() response: {data}")
    except Exception as e:
        logging.error(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

if __name__ == "__main__":
    asyncio.run(exchange_info())
