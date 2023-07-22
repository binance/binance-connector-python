#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    params = {
        "algo": "sha256",
        "userName": "user_name",
        "startDate": 1607659086000,
        "endDate": 1617659086000,
        "toPoolUser": "pool_user_name",
        "hashRate": "100000000",
    }

    client = Client(api_key, api_secret)
    logging.info(await client.mining_hashrate_resale_request(**params))


if __name__ == "__main__":
    asyncio.run(main())
