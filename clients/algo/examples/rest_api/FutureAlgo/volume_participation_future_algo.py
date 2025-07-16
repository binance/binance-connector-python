import os
import logging

from binance_algo.algo import Algo, ConfigurationRestAPI, ALGO_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", ALGO_REST_API_PROD_URL),
)

# Initialize Algo client
client = Algo(config_rest_api=configuration_rest_api)


def volume_participation_future_algo():
    try:
        response = client.rest_api.volume_participation_future_algo(
            symbol="BTCUSDT",
            side="BUY",
            quantity=1.0,
            urgency="LOW",
        )

        rate_limits = response.rate_limits
        logging.info(f"volume_participation_future_algo() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"volume_participation_future_algo() response: {data}")
    except Exception as e:
        logging.error(f"volume_participation_future_algo() error: {e}")


if __name__ == "__main__":
    volume_participation_future_algo()
