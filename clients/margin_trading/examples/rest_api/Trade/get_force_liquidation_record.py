import os
import logging

from binance_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MARGIN_TRADING_REST_API_PROD_URL),
)

# Initialize MarginTrading client
client = MarginTrading(config_rest_api=configuration_rest_api)


def get_force_liquidation_record():
    try:
        response = client.rest_api.get_force_liquidation_record()

        rate_limits = response.rate_limits
        logging.info(f"get_force_liquidation_record() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_force_liquidation_record() response: {data}")
    except Exception as e:
        logging.error(f"get_force_liquidation_record() error: {e}")


if __name__ == "__main__":
    get_force_liquidation_record()
