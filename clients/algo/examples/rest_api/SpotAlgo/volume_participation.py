import os
import logging

from binance_sdk_algo.algo import Algo, ConfigurationRestAPI, ALGO_REST_API_PROD_URL
from binance_sdk_algo.rest_api.models import VolumeParticipationSideEnum
from binance_sdk_algo.rest_api.models import VolumeParticipationUrgencyEnum

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", ALGO_REST_API_PROD_URL),
)

# Initialize Algo client
client = Algo(config_rest_api=configuration_rest_api)


def volume_participation():
    try:
        response = client.rest_api.volume_participation(
            symbol="BTCUSDT",
            side=VolumeParticipationSideEnum["BUY"].value,
            quantity=1,
            urgency=VolumeParticipationUrgencyEnum["LOW"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"volume_participation() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"volume_participation() response: {data}")
    except Exception as e:
        logging.error(f"volume_participation() error: {e}")


if __name__ == "__main__":
    volume_participation()
