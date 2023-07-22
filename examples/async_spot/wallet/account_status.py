#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

async def main():
    api_key = "api_key"
    private_key = "./private_key.txt"
    private_key_pass = "private key password (if applicable)"

    with open(private_key, "rb") as f:
        private_key = f.read()

    spot_client = Client(
        api_key=api_key,
        private_key=private_key,
        private_key_pass=private_key_pass,
        key_type="ed25519",
    )
    logging.info(await spot_client.account_status())


if __name__ == "__main__":
    asyncio.run(main())
