import os
import logging

from binance_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MARGIN_TRADING_REST_API_PROD_URL),
)

# Initialize MarginTrading client
client = MarginTrading(config_rest_api=configuration_rest_api)


def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode():
    try:
        response = (
            client.rest_api.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode()
        )

        rate_limits = response.rate_limits
        logging.info(
            f"query_liability_coin_leverage_bracket_in_cross_margin_pro_mode() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(
            f"query_liability_coin_leverage_bracket_in_cross_margin_pro_mode() response: {data}"
        )
    except Exception as e:
        logging.error(
            f"query_liability_coin_leverage_bracket_in_cross_margin_pro_mode() error: {e}"
        )


if __name__ == "__main__":
    query_liability_coin_leverage_bracket_in_cross_margin_pro_mode()
