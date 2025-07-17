import os
import logging

from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingUsdsFutures client
client = DerivativesTradingUsdsFutures(config_rest_api=configuration_rest_api)


def accept_the_offered_quote():
    try:
        response = client.rest_api.accept_the_offered_quote(
            quote_id="1",
        )

        rate_limits = response.rate_limits
        logging.info(f"accept_the_offered_quote() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"accept_the_offered_quote() response: {data}")
    except Exception as e:
        logging.error(f"accept_the_offered_quote() error: {e}")


if __name__ == "__main__":
    accept_the_offered_quote()
