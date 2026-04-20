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


def aggregated_trades():
    try:
        response = client.rest_api.aggregated_trades(
            symbol="symbol_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"aggregated_trades() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"aggregated_trades() response: {data}")
    except Exception as e:
        logging.error(f"aggregated_trades() error: {e}")


if __name__ == "__main__":
    aggregated_trades()
