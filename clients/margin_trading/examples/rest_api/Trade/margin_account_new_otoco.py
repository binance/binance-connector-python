import os
import logging

from binance_sdk_margin_trading.margin_trading import (
    MarginTrading,
    ConfigurationRestAPI,
    MARGIN_TRADING_REST_API_PROD_URL,
)
from binance_sdk_margin_trading.rest_api.models import (
    MarginAccountNewOtocoWorkingTypeEnum,
)
from binance_sdk_margin_trading.rest_api.models import (
    MarginAccountNewOtocoWorkingSideEnum,
)
from binance_sdk_margin_trading.rest_api.models import (
    MarginAccountNewOtocoPendingSideEnum,
)
from binance_sdk_margin_trading.rest_api.models import (
    MarginAccountNewOtocoPendingAboveTypeEnum,
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


def margin_account_new_otoco():
    try:
        response = client.rest_api.margin_account_new_otoco(
            symbol="BTCUSDT",
            working_type=MarginAccountNewOtocoWorkingTypeEnum["LIMIT"].value,
            working_side=MarginAccountNewOtocoWorkingSideEnum["SELL"].value,
            working_price=1.0,
            working_quantity=1.0,
            pending_side=MarginAccountNewOtocoPendingSideEnum["BUY"].value,
            pending_quantity=1.0,
            pending_above_type=MarginAccountNewOtocoPendingAboveTypeEnum[
                "LIMIT_MAKER"
            ].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"margin_account_new_otoco() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"margin_account_new_otoco() response: {data}")
    except Exception as e:
        logging.error(f"margin_account_new_otoco() error: {e}")


if __name__ == "__main__":
    margin_account_new_otoco()
