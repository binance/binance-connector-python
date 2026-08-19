import os
import logging

from binance_sdk_stocks.stocks import (
    Stocks,
    ConfigurationRestAPI,
    STOCKS_REST_API_PROD_URL,
)
from binance_sdk_stocks.rest_api.models import TokenizedConvertStatusConvertTypeEnum


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", STOCKS_REST_API_PROD_URL),
)

# Initialize Stocks client
client = Stocks(config_rest_api=configuration_rest_api)


def tokenized_convert_status():
    try:
        response = client.rest_api.tokenized_convert_status(
            issuer_request_id="mint-20260505-8f3b9e1a2d3c4b5a",
            convert_type=TokenizedConvertStatusConvertTypeEnum["MINT"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"tokenized_convert_status() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"tokenized_convert_status() response: {data}")
    except Exception as e:
        logging.error(f"tokenized_convert_status() error: {e}")


if __name__ == "__main__":
    tokenized_convert_status()
