import os
import logging

from binance_sdk_c2c.c2c import C2C, ConfigurationRestAPI, C2C_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", C2C_REST_API_PROD_URL),
)

# Initialize C2C client
client = C2C(config_rest_api=configuration_rest_api)


def get_c2_c_trade_history():
    try:
        response = client.rest_api.get_c2_c_trade_history()

        rate_limits = response.rate_limits
        logging.info(f"get_c2_c_trade_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_c2_c_trade_history() response: {data}")
    except Exception as e:
        logging.error(f"get_c2_c_trade_history() error: {e}")


if __name__ == "__main__":
    get_c2_c_trade_history()
