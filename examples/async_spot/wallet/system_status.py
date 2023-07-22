#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

async def main():
    spot_client = Client()

    logging.info(await spot_client.system_status())


if __name__ == "__main__":
    asyncio.run(main())
