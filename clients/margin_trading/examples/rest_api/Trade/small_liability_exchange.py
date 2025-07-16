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


def small_liability_exchange():
    try:
        response = client.rest_api.small_liability_exchange(
            asset_names=["BTC"],
        )

        rate_limits = response.rate_limits
        logging.info(f"small_liability_exchange() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"small_liability_exchange() response: {data}")
    except Exception as e:
        logging.error(f"small_liability_exchange() error: {e}")


if __name__ == "__main__":
    small_liability_exchange()
