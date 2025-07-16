from enum import Enum


# TimeUnit Constants
class TimeUnit(Enum):
    MILLISECOND = "MILLISECOND"
    millisecond = "millisecond"
    MICROSECOND = "MICROSECOND"
    microsecond = "microsecond"

class WebsocketMode(Enum):
    SINGLE = "single"
    POOL = "pool"

# Algo constants
ALGO_REST_API_PROD_URL = "https://api.binance.com"

# Auto Invest constants
AUTO_INVEST_REST_API_PROD_URL = "https://api.binance.com"

# C2C constants
C2C_REST_API_PROD_URL = "https://api.binance.com"

# Convert constants
CONVERT_REST_API_PROD_URL = "https://api.binance.com"

# Copy Trading constants
COPY_TRADING_REST_API_PROD_URL = "https://api.binance.com"

# Crypto Loan constants
CRYPTO_LOAN_REST_API_PROD_URL = "https://api.binance.com"

# Derivatives Trading constants
DERIVATIVES_TRADING_REST_API_PROD_URL = "https://api.binance.com"

# Derivatives Trading (COIN-M Futures) constants
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL = "https://dapi.binance.com"
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_TESTNET_URL = "https://testnet.binancefuture.com"
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL = "wss://ws-dapi.binance.com/ws-dapi/v1"
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_TESTNET_URL = "wss://testnet.binancefuture.com/ws-dapi/v1"
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_PROD_URL = "wss://dstream.binance.com"
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_TESTNET_URL = "wss://dstream.binancefuture.com"

# Derivatives Trading (USDS Futures) constants
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL = "https://fapi.binance.com"
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_TESTNET_URL = "https://testnet.binancefuture.com"
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_PROD_URL = "wss://ws-fapi.binance.com/ws-fapi/v1"
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_TESTNET_URL = "wss://testnet.binancefuture.com/ws-fapi/v1"
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_PROD_URL = "wss://fstream.binance.com"
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_TESTNET_URL = "wss://stream.binancefuture.com"

# Derivatives Trading (Options) constants
DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL = "https://eapi.binance.com"
DERIVATIVES_TRADING_OPTIONS_WS_STREAMS_PROD_URL = "wss://nbstream.binance.com/eoptions"

# Derivatives Trading (Portfolio Margin) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL = "https://papi.binance.com"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_TESTNET_URL = "https://testnet.binancefuture.com"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_WS_STREAMS_PROD_URL = "wss://fstream.binance.com/pm"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_WS_STREAMS_TESTNET_URL = "wss://fstream.binancefuture.com/pm"

# Derivatives Trading (Portfolio Margin Pro) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_REST_API_PROD_URL = "https://api.binance.com"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_WS_STREAMS_PROD_URL = "wss://fstream.binance.com/pm-classic"

# Dual Investment constants
DUAL_INVESTMENT_REST_API_PROD_URL = "https://api.binance.com"

# Fiat constants
FIAT_REST_API_PROD_URL = "https://api.binance.com"

# Gift Card constants
GIFT_CARD_REST_API_PROD_URL = "https://api.binance.com"

# Margin Trading constants
MARGIN_TRADING_REST_API_PROD_URL = "https://api.binance.com"
MARGIN_TRADING_WS_STREAMS_PROD_URL = "wss://stream.binance.com:9443"
MARGIN_TRADING_RISK_WS_STREAMS_PROD_URL = "wss://margin-stream.binance.com"

# Mining constants
MINING_REST_API_PROD_URL = "https://api.binance.com"

# NFT constants
NFT_REST_API_PROD_URL = "https://api.binance.com"

# Pay constants
PAY_REST_API_PROD_URL = "https://api.binance.com"

# Rebate constants
REBATE_REST_API_PROD_URL = "https://api.binance.com"

# Simple Earn constants
SIMPLE_EARN_REST_API_PROD_URL = "https://api.binance.com"

# Spot Constants
SPOT_REST_API_PROD_URL = "https://api.binance.com"
SPOT_REST_API_TESTNET_URL = "https://testnet.binance.vision"
SPOT_WS_API_PROD_URL = "wss://ws-api.binance.com:443/ws-api/v3"
SPOT_WS_API_TESTNET_URL = "wss://ws-api.testnet.binance.vision/ws-api/v3"
SPOT_WS_STREAMS_PROD_URL = "wss://stream.binance.com:9443"
SPOT_WS_STREAMS_TESTNET_URL = "wss://stream.testnet.binance.vision"
SPOT_REST_API_MARKET_URL = "https://data-api.binance.vision"
SPOT_WS_STREAMS_MARKET_URL = "wss://data-stream.binance.vision"

# Staking constants
STAKING_REST_API_PROD_URL = "https://api.binance.com"

# Sub Account constants
SUB_ACCOUNT_REST_API_PROD_URL = "https://api.binance.com"

# VIP Loan constants
VIP_LOAN_REST_API_PROD_URL = "https://api.binance.com"

# Wallet constants
WALLET_REST_API_PROD_URL = "https://api.binance.com"
