import os
import logging

from binance_sdk_derivatives_trading_options.derivatives_trading_options import (
    DerivativesTradingOptions,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL),
)

# Initialize DerivativesTradingOptions client
client = DerivativesTradingOptions(config_rest_api=configuration_rest_api)


def user_exercise_record():
    try:
        response = client.rest_api.user_exercise_record()

        rate_limits = response.rate_limits
        logging.info(f"user_exercise_record() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"user_exercise_record() response: {data}")
    except Exception as e:
        logging.error(f"user_exercise_record() error: {e}")


if __name__ == "__main__":
    user_exercise_record()
