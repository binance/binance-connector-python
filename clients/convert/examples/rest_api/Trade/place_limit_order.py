import os
import logging

from binance_sdk_convert.convert import (
    Convert,
    ConfigurationRestAPI,
    CONVERT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", CONVERT_REST_API_PROD_URL),
)

# Initialize Convert client
client = Convert(config_rest_api=configuration_rest_api)


def place_limit_order():
    try:
        response = client.rest_api.place_limit_order(
            base_asset="base_asset_example",
            quote_asset="quote_asset_example",
            limit_price=1.0,
            side="BUY",
            expired_type="expired_type_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"place_limit_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"place_limit_order() response: {data}")
    except Exception as e:
        logging.error(f"place_limit_order() error: {e}")


if __name__ == "__main__":
    place_limit_order()
