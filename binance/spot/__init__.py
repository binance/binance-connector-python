from binance.api import API


class Spot(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.spot.market import ping
    from binance.spot.market import time
    from binance.spot.market import exchange_info
    from binance.spot.market import depth
    from binance.spot.market import trades
    from binance.spot.market import historical_trades
    from binance.spot.market import agg_trades
    from binance.spot.market import klines
    from binance.spot.market import ui_klines
    from binance.spot.market import avg_price
    from binance.spot.market import ticker_24hr
    from binance.spot.market import ticker_price
    from binance.spot.market import book_ticker
    from binance.spot.market import rolling_window_ticker

    # ACCOUNT (including orders and trades)
    from binance.spot.trade import new_order_test
    from binance.spot.trade import new_order
    from binance.spot.trade import cancel_order
    from binance.spot.trade import cancel_open_orders
    from binance.spot.trade import get_order
    from binance.spot.trade import cancel_and_replace
    from binance.spot.trade import get_open_orders
    from binance.spot.trade import get_orders
    from binance.spot.trade import new_oco_order
    from binance.spot.trade import cancel_oco_order
    from binance.spot.trade import get_oco_order
    from binance.spot.trade import get_oco_orders
    from binance.spot.trade import get_oco_open_orders
    from binance.spot.trade import account
    from binance.spot.trade import my_trades
    from binance.spot.trade import get_order_rate_limit

    # STREAMS
    from binance.spot.data_stream import new_listen_key
    from binance.spot.data_stream import renew_listen_key
    from binance.spot.data_stream import close_listen_key
    from binance.spot.data_stream import new_margin_listen_key
    from binance.spot.data_stream import renew_margin_listen_key
    from binance.spot.data_stream import close_margin_listen_key
    from binance.spot.data_stream import new_isolated_margin_listen_key
    from binance.spot.data_stream import renew_isolated_margin_listen_key
    from binance.spot.data_stream import close_isolated_margin_listen_key

    # MARGIN
    from binance.spot.margin import margin_transfer
    from binance.spot.margin import margin_borrow
    from binance.spot.margin import margin_repay
    from binance.spot.margin import margin_asset
    from binance.spot.margin import margin_pair
    from binance.spot.margin import margin_all_assets
    from binance.spot.margin import margin_all_pairs
    from binance.spot.margin import margin_pair_index
    from binance.spot.margin import new_margin_order
    from binance.spot.margin import cancel_margin_order
    from binance.spot.margin import margin_transfer_history
    from binance.spot.margin import margin_load_record
    from binance.spot.margin import margin_repay_record
    from binance.spot.margin import margin_interest_history
    from binance.spot.margin import margin_force_liquidation_record
    from binance.spot.margin import margin_account
    from binance.spot.margin import margin_order
    from binance.spot.margin import margin_open_orders
    from binance.spot.margin import margin_open_orders_cancellation
    from binance.spot.margin import margin_all_orders
    from binance.spot.margin import margin_my_trades
    from binance.spot.margin import margin_max_borrowable
    from binance.spot.margin import margin_max_transferable
    from binance.spot.margin import isolated_margin_transfer
    from binance.spot.margin import isolated_margin_transfer_history
    from binance.spot.margin import isolated_margin_account
    from binance.spot.margin import isolated_margin_pair
    from binance.spot.margin import isolated_margin_all_pairs
    from binance.spot.margin import toggle_bnbBurn
    from binance.spot.margin import bnbBurn_status
    from binance.spot.margin import margin_interest_rate_history
    from binance.spot.margin import new_margin_oco_order
    from binance.spot.margin import cancel_margin_oco_order
    from binance.spot.margin import get_margin_oco_order
    from binance.spot.margin import get_margin_oco_orders
    from binance.spot.margin import get_margin_open_oco_orders
    from binance.spot.margin import cancel_isolated_margin_account
    from binance.spot.margin import enable_isolated_margin_account
    from binance.spot.margin import isolated_margin_account_limit
    from binance.spot.margin import margin_fee
    from binance.spot.margin import isolated_margin_fee
    from binance.spot.margin import isolated_margin_tier
    from binance.spot.margin import margin_order_usage
    from binance.spot.margin import margin_dust_log

    # SAVINGS
    from binance.spot.savings import savings_flexible_products
    from binance.spot.savings import savings_flexible_user_left_quota
    from binance.spot.savings import savings_purchase_flexible_product
    from binance.spot.savings import savings_flexible_user_redemption_quota
    from binance.spot.savings import savings_flexible_redeem
    from binance.spot.savings import savings_flexible_product_position
    from binance.spot.savings import savings_project_list
    from binance.spot.savings import savings_purchase_project
    from binance.spot.savings import savings_project_position
    from binance.spot.savings import savings_account
    from binance.spot.savings import savings_purchase_record
    from binance.spot.savings import savings_redemption_record
    from binance.spot.savings import savings_interest_history
    from binance.spot.savings import savings_change_position

    # Staking
    from binance.spot.staking import staking_product_list
    from binance.spot.staking import staking_purchase_product
    from binance.spot.staking import staking_redeem_product
    from binance.spot.staking import staking_product_position
    from binance.spot.staking import staking_history
    from binance.spot.staking import staking_set_auto_staking
    from binance.spot.staking import staking_product_quota

    # WALLET
    from binance.spot.wallet import system_status
    from binance.spot.wallet import coin_info
    from binance.spot.wallet import account_snapshot
    from binance.spot.wallet import disable_fast_withdraw
    from binance.spot.wallet import enable_fast_withdraw
    from binance.spot.wallet import withdraw
    from binance.spot.wallet import deposit_history
    from binance.spot.wallet import withdraw_history
    from binance.spot.wallet import deposit_address
    from binance.spot.wallet import account_status
    from binance.spot.wallet import api_trading_status
    from binance.spot.wallet import dust_log
    from binance.spot.wallet import user_universal_transfer
    from binance.spot.wallet import user_universal_transfer_history
    from binance.spot.wallet import transfer_dust
    from binance.spot.wallet import asset_dividend_record
    from binance.spot.wallet import asset_detail
    from binance.spot.wallet import trade_fee
    from binance.spot.wallet import funding_wallet
    from binance.spot.wallet import user_asset
    from binance.spot.wallet import api_key_permissions
    from binance.spot.wallet import bnb_convertible_assets

    # MINING
    from binance.spot.mining import mining_algo_list
    from binance.spot.mining import mining_coin_list
    from binance.spot.mining import mining_worker
    from binance.spot.mining import mining_worker_list
    from binance.spot.mining import mining_earnings_list
    from binance.spot.mining import mining_bonus_list
    from binance.spot.mining import mining_statistics_list
    from binance.spot.mining import mining_account_list
    from binance.spot.mining import mining_hashrate_resale_request
    from binance.spot.mining import mining_hashrate_resale_cancellation
    from binance.spot.mining import mining_hashrate_resale_list
    from binance.spot.mining import mining_hashrate_resale_details
    from binance.spot.mining import mining_account_earning

    # SUB-ACCOUNT
    from binance.spot.sub_account import sub_account_create
    from binance.spot.sub_account import sub_account_list
    from binance.spot.sub_account import sub_account_assets
    from binance.spot.sub_account import sub_account_deposit_address
    from binance.spot.sub_account import sub_account_deposit_history
    from binance.spot.sub_account import sub_account_status
    from binance.spot.sub_account import sub_account_enable_margin
    from binance.spot.sub_account import sub_account_margin_account
    from binance.spot.sub_account import sub_account_margin_account_summary
    from binance.spot.sub_account import sub_account_enable_futures
    from binance.spot.sub_account import sub_account_futures_transfer
    from binance.spot.sub_account import sub_account_margin_transfer
    from binance.spot.sub_account import sub_account_transfer_to_sub
    from binance.spot.sub_account import sub_account_transfer_to_master
    from binance.spot.sub_account import sub_account_transfer_sub_account_history
    from binance.spot.sub_account import sub_account_futures_asset_transfer_history
    from binance.spot.sub_account import sub_account_futures_asset_transfer
    from binance.spot.sub_account import sub_account_spot_summary
    from binance.spot.sub_account import sub_account_universal_transfer
    from binance.spot.sub_account import sub_account_universal_transfer_history
    from binance.spot.sub_account import sub_account_futures_account
    from binance.spot.sub_account import sub_account_futures_account_summary
    from binance.spot.sub_account import sub_account_futures_position_risk
    from binance.spot.sub_account import sub_account_spot_transfer_history
    from binance.spot.sub_account import sub_account_enable_leverage_token
    from binance.spot.sub_account import managed_sub_account_deposit
    from binance.spot.sub_account import managed_sub_account_assets
    from binance.spot.sub_account import managed_sub_account_withdraw
    from binance.spot.sub_account import sub_account_api_toggle_ip_restriction
    from binance.spot.sub_account import sub_account_api_add_ip
    from binance.spot.sub_account import sub_account_api_get_ip_restriction
    from binance.spot.sub_account import sub_account_api_delete_ip
    from binance.spot.sub_account import managed_sub_account_get_snapshot

    # FUTURES
    from binance.spot.futures import futures_transfer
    from binance.spot.futures import futures_transfer_history
    from binance.spot.futures import futures_loan_borrow
    from binance.spot.futures import futures_loan_borrow_history
    from binance.spot.futures import futures_loan_repay
    from binance.spot.futures import futures_loan_repay_history
    from binance.spot.futures import futures_loan_wallet
    from binance.spot.futures import futures_loan_configs
    from binance.spot.futures import futures_loan_calc_adjust_level
    from binance.spot.futures import futures_loan_calc_max_adjust_amount
    from binance.spot.futures import futures_loan_adjust_collateral
    from binance.spot.futures import futures_loan_adjust_collateral_history
    from binance.spot.futures import futures_loan_liquidation_history
    from binance.spot.futures import futures_loan_collateral_repay_limit
    from binance.spot.futures import futures_loan_collateral_repay_quote
    from binance.spot.futures import futures_loan_collateral_repay
    from binance.spot.futures import futures_loan_collateral_repay_result
    from binance.spot.futures import futures_loan_interest_history

    # BLVTs
    from binance.spot.blvt import blvt_info
    from binance.spot.blvt import subscribe_blvt
    from binance.spot.blvt import subscription_record
    from binance.spot.blvt import redeem_blvt
    from binance.spot.blvt import redemption_record
    from binance.spot.blvt import user_limit_info

    # BSwap
    from binance.spot.bswap import bswap_pools
    from binance.spot.bswap import bswap_liquidity
    from binance.spot.bswap import bswap_liquidity_add
    from binance.spot.bswap import bswap_liquidity_remove
    from binance.spot.bswap import bswap_liquidity_operation_record
    from binance.spot.bswap import bswap_request_quote
    from binance.spot.bswap import bswap_swap
    from binance.spot.bswap import bswap_swap_history
    from binance.spot.bswap import bswap_pool_configure
    from binance.spot.bswap import bswap_add_liquidity_preview
    from binance.spot.bswap import bswap_remove_liquidity_preview
    from binance.spot.bswap import bswap_unclaimed_rewards
    from binance.spot.bswap import bswap_claim_rewards
    from binance.spot.bswap import bswap_claimed_rewards

    # FIAT
    from binance.spot.fiat import fiat_order_history
    from binance.spot.fiat import fiat_payment_history

    # C2C
    from binance.spot.c2c import c2c_trade_history

    # CRYPTO LOANS
    from binance.spot.loan import loan_history
    from binance.spot.loan import loan_borrow
    from binance.spot.loan import loan_borrow_history
    from binance.spot.loan import loan_ongoing_orders
    from binance.spot.loan import loan_repay
    from binance.spot.loan import loan_repay_history
    from binance.spot.loan import loan_adjust_ltv
    from binance.spot.loan import loan_adjust_ltv_history

    # PAY
    from binance.spot.pay import pay_history

    # CONVERT
    from binance.spot.convert import convert_trade_history

    # REBATE
    from binance.spot.rebate import rebate_spot_history

    # NFT
    from binance.spot.nft import nft_transaction_history
    from binance.spot.nft import nft_deposit_history
    from binance.spot.nft import nft_withdraw_history
    from binance.spot.nft import nft_asset

    # Gift Card (Binance Code in the API documentation)
    from binance.spot.gift_card import gift_card_create_code
    from binance.spot.gift_card import gift_card_redeem_code
    from binance.spot.gift_card import gift_card_verify_code
    from binance.spot.gift_card import gift_card_rsa_public_key

    # Portfolio Margin
    from binance.spot.portfolio_margin import portfolio_margin_account
    from binance.spot.portfolio_margin import portfolio_margin_collateral_rate
    from binance.spot.portfolio_margin import portfolio_margin_bankruptcy_loan_amount
    from binance.spot.portfolio_margin import portfolio_margin_bankruptcy_loan_repay
