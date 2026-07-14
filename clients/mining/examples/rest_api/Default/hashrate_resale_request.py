import os
import logging

from binance_sdk_mining.mining import (
    Mining,
    ConfigurationRestAPI,
    MINING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MINING_REST_API_PROD_URL),
)

# Initialize Mining client
client = Mining(config_rest_api=configuration_rest_api)


def hashrate_resale_request():
    try:
        response = client.rest_api.hashrate_resale_request(
            user_name="test",
            algo="sha256",
            end_date=1770736694138,
            start_date=1770736694138,
            to_pool_user="S19pro",
            hash_rate=100000000,
        )

        rate_limits = response.rate_limits
        logging.info(f"hashrate_resale_request() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"hashrate_resale_request() response: {data}")
    except Exception as e:
        logging.error(f"hashrate_resale_request() error: {e}")


if __name__ == "__main__":
    hashrate_resale_request()
