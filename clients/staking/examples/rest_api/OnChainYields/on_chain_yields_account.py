import os
import logging

from binance_staking.staking import (
    Staking,
    ConfigurationRestAPI,
    STAKING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", STAKING_REST_API_PROD_URL),
)

# Initialize Staking client
client = Staking(config_rest_api=configuration_rest_api)


def on_chain_yields_account():
    try:
        response = client.rest_api.on_chain_yields_account()

        rate_limits = response.rate_limits
        logging.info(f"on_chain_yields_account() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"on_chain_yields_account() response: {data}")
    except Exception as e:
        logging.error(f"on_chain_yields_account() error: {e}")


if __name__ == "__main__":
    on_chain_yields_account()
