# Binance Python Connectors

[![Build Status](https://img.shields.io/github/actions/workflow/status/binance/binance-connector-python/ci.yaml)](https://github.com/binance/binance-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/binance/binance-connector-python)](https://github.com/binance/binance-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![Known Vulnerabilities](https://snyk.io/test/github/binance/binance-connector-python/badge.svg)](https://snyk.io/test/github/binance/binance-connector-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Collection of auto-generated Python connectors for Binance APIs.

## Prerequisites

Before using the connectors, ensure you have:

- **Python** (version 3.9 or later)
- **pip** (Python package manager)
- **poetry** ()


## Available Connectors

- [binance-algo](./clients/algo) - Algo Trading connector
- [binance-c2c](./clients/c2c/) - C2C connector
- [binance-convert](./clients/convert/) - Convert connector
- [binance-copy-trading](./clients/copy_trading/) - Copy Trading connector
- [binance-crypto-loan](./clients/crypto_loan/) - Crypto Loan connector
- [binance-derivatives-trading-coin-futures](./clients/derivatives_trading_coin_futures/) - Coin Futures Trading connector
- [binance-derivatives-trading-options](./clients/derivatives_trading_options/) - Options Trading connector
- [binance-derivatives-trading-portfolio-margin](./clients/derivatives_trading_portfolio_margin/) - Portfolio Margin Futures Trading connector
- [binance-derivatives-trading-portfolio-margin-pro](./clients/derivatives_trading_portfolio_margin_pro/) - Portfolio Margin Pro Trading connector
- [binance-derivatives-trading-usds-futures](./clients/derivatives_trading_usds_futures/) - USDs Futures Trading connector
- [binance-dual-investment](./clients/dual_investment/) - Dual Investment connector
- [binance-fiat](./clients/fiat/) - Fiat connector
- [binance-gift-card](./clients/gift_card/) - Gift Card connector
- [binance-margin-trading](./clients/margin_trading/) - Margin Trading connector
- [binance-mining](./clients/mining/) - Mining connector
- [binance-nft](./clients/nft/) - NFT connector
- [binance-pay](./clients/pay/) - Pay connector
- [binance-rebate](./clients/rebate/) - Rebate connector
- [binance-simple-earn](./clients/simple_earn/) - Simple Earn connector
- [binance-spot](./clients/spot/) - Spot Trading connector
- [binance-staking](./clients/staking/) - Staking connector
- [binance-sub-account](./clients/sub_account/) - Sub Account connector
- [binance-vip-loan](./clients/vip_loan/) - VIP Loan connector
- [binance-wallet](./clients/wallet/) - Wallet connector

## Documentation

For detailed information, refer to the [Binance API Documentation](https://developers.binance.com).

## Installation

Each connector is published as a separate Python package. You can install them via `pip` or `poetry`. For example:

```bash
pip install binance-spot
```

```bash
poetry add binance-spot
```

Or to install multiple connectors:

```bash
pip install binance-spot binance-margin-trading binance-staking
```

```bash
poetry add binance-spot binance-margin-trading binance-staking
```

## Contributing

Since this repository contains auto-generated code using OpenAPI Generator, we encourage you to:

1. Open a GitHub issue to discuss your ideas or report bugs
2. Allow maintainers to implement necessary changes through the code generation process

## Code Style

This repository follows **PEP 8** standards and enforces **Black** for formatting. Before submitting a pull request, format your code:

```bash
black .
```

Run type checks:

```bash
mypy .
```

## Migration Guide

If you're upgrading from the previous unified connector, refer to our [Migration Guide](./MIGRATION.md) for detailed steps on transitioning to the new modular structure.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENCE) file for details.
