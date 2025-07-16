import os
import logging

from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_rest_api=configuration_rest_api)


def ticker24hr_price_change_statistics():
    try:
        response = client.rest_api.ticker24hr_price_change_statistics()

        rate_limits = response.rate_limits
        logging.info(f"ticker24hr_price_change_statistics() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"ticker24hr_price_change_statistics() response: {data}")
    except Exception as e:
        logging.error(f"ticker24hr_price_change_statistics() error: {e}")


if __name__ == "__main__":
    ticker24hr_price_change_statistics()
