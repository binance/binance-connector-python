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


def subscribe_on_chain_yields_locked_product():
    try:
        response = client.rest_api.subscribe_on_chain_yields_locked_product(
            project_id="1",
            amount=1.0,
        )

        rate_limits = response.rate_limits
        logging.info(
            f"subscribe_on_chain_yields_locked_product() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"subscribe_on_chain_yields_locked_product() response: {data}")
    except Exception as e:
        logging.error(f"subscribe_on_chain_yields_locked_product() error: {e}")


if __name__ == "__main__":
    subscribe_on_chain_yields_locked_product()
