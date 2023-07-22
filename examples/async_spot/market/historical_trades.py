#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, _ = get_api_key()

    # historical_trades requires api key in request header
    spot_client = Client(api_key=api_key, base_url="https://testnet.binance.vision")

    logging.info(await spot_client.historical_trades("BTCUSDT"))
    logging.info(await spot_client.historical_trades("BTCUSDT", limit=10, fromId=""))



if __name__ == "__main__":
    asyncio.run(main())

