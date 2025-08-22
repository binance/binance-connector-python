import asyncio
import os
import logging

from binance_sdk_spot.spot import Spot, SPOT_WS_API_PROD_URL, ConfigurationWebSocketAPI


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


async def user_data_stream_subscribe_signature():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        res = await connection.user_data_stream_subscribe_signature()
        response = res.response

        rate_limits = response.rate_limits
        logging.info(
            f"user_data_stream_subscribe_signature() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"user_data_stream_subscribe_signature() response: {data}")

        res.stream.on("message", lambda data: print(f"{data}"))
        await asyncio.sleep(10)
        await res.stream.unsubscribe()

    except Exception as e:
        logging.error(f"user_data_stream_subscribe_signature() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(user_data_stream_subscribe_signature())
