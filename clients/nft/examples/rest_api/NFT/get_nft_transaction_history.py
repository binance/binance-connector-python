import os
import logging

from binance_sdk_nft.nft import NFT, ConfigurationRestAPI, NFT_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", NFT_REST_API_PROD_URL),
)

# Initialize NFT client
client = NFT(config_rest_api=configuration_rest_api)


def get_nft_transaction_history():
    try:
        response = client.rest_api.get_nft_transaction_history(
            order_type=56,
        )

        rate_limits = response.rate_limits
        logging.info(f"get_nft_transaction_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_nft_transaction_history() response: {data}")
    except Exception as e:
        logging.error(f"get_nft_transaction_history() error: {e}")


if __name__ == "__main__":
    get_nft_transaction_history()
