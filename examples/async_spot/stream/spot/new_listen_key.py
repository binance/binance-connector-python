#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, _ = get_api_key()

    client = Client(api_key, base_url="https://testnet.binance.vision")
    logging.info(await client.new_listen_key())


if __name__ == "__main__":
    asyncio.run(main())
