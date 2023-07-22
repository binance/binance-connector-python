import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

async def main():
    spot_client = Client()

    logging.info(await spot_client.exchange_info())

    logging.info(await spot_client.exchange_info(symbol="BNBUSDT"))
    logging.info(await spot_client.exchange_info(symbols=["BTCUSDT", "BNBUSDT"]))

    logging.info(await spot_client.exchange_info(permissions=["MARGIN"]))
    logging.info(await spot_client.exchange_info(permissions=["MARGIN", "LEVERAGED"]))
    

if __name__ == "__main__":
    asyncio.run(main())

