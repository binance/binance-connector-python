#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

async def main():
    spot_client = Client(base_url="https://testnet.binance.vision")

    logging.info(await spot_client.ticker_24hr("BTCUSDT", symbols=None, type="MINI"))
    logging.info(
        await spot_client.ticker_24hr(symbol=None, symbols=["BTCUSDT", "BNBUSDT"], type="FULL")
    )


if __name__ == "__main__":
    asyncio.run(main())

