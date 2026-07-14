import os
import logging

from binance_sdk_alpha.alpha import Alpha, ConfigurationRestAPI, ALPHA_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", ALPHA_REST_API_PROD_URL),
)

# Initialize Alpha client
client = Alpha(config_rest_api=configuration_rest_api)


def full_depth():
    try:
        response = client.rest_api.full_depth(
            symbol="ALPHA_175USDT",
        )

        rate_limits = response.rate_limits
        logging.info(f"full_depth() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"full_depth() response: {data}")
    except Exception as e:
        logging.error(f"full_depth() error: {e}")


if __name__ == "__main__":
    full_depth()
