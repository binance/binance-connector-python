import os
import logging

from binance_copy_trading.copy_trading import (
    CopyTrading,
    ConfigurationRestAPI,
    COPY_TRADING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", COPY_TRADING_REST_API_PROD_URL),
)

# Initialize CopyTrading client
client = CopyTrading(config_rest_api=configuration_rest_api)


def get_futures_lead_trading_symbol_whitelist():
    try:
        response = client.rest_api.get_futures_lead_trading_symbol_whitelist()

        rate_limits = response.rate_limits
        logging.info(
            f"get_futures_lead_trading_symbol_whitelist() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"get_futures_lead_trading_symbol_whitelist() response: {data}")
    except Exception as e:
        logging.error(f"get_futures_lead_trading_symbol_whitelist() error: {e}")


if __name__ == "__main__":
    get_futures_lead_trading_symbol_whitelist()
