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


def query_margin_accounts_all_oco():
    try:
        response = client.rest_api.query_margin_accounts_all_oco()

        rate_limits = response.rate_limits
        logging.info(f"query_margin_accounts_all_oco() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_margin_accounts_all_oco() response: {data}")
    except Exception as e:
        logging.error(f"query_margin_accounts_all_oco() error: {e}")


if __name__ == "__main__":
    query_margin_accounts_all_oco()
