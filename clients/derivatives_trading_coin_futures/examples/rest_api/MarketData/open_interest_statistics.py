import os
import logging

from binance_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL,
)
from binance_derivatives_trading_coin_futures.rest_api.models import (
    OpenInterestStatisticsContractTypeEnum,
)
from binance_derivatives_trading_coin_futures.rest_api.models import (
    OpenInterestStatisticsPeriodEnum,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_rest_api=configuration_rest_api)


def open_interest_statistics():
    try:
        response = client.rest_api.open_interest_statistics(
            pair="pair_example",
            contract_type=OpenInterestStatisticsContractTypeEnum["PERPETUAL"].value,
            period=OpenInterestStatisticsPeriodEnum["PERIOD_5m"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"open_interest_statistics() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"open_interest_statistics() response: {data}")
    except Exception as e:
        logging.error(f"open_interest_statistics() error: {e}")


if __name__ == "__main__":
    open_interest_statistics()
