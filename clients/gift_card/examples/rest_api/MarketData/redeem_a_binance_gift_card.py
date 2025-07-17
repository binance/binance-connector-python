import os
import logging

from binance_sdk_gift_card.gift_card import (
    GiftCard,
    ConfigurationRestAPI,
    GIFT_CARD_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", GIFT_CARD_REST_API_PROD_URL),
)

# Initialize GiftCard client
client = GiftCard(config_rest_api=configuration_rest_api)


def redeem_a_binance_gift_card():
    try:
        response = client.rest_api.redeem_a_binance_gift_card(
            code="code_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"redeem_a_binance_gift_card() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"redeem_a_binance_gift_card() response: {data}")
    except Exception as e:
        logging.error(f"redeem_a_binance_gift_card() error: {e}")


if __name__ == "__main__":
    redeem_a_binance_gift_card()
