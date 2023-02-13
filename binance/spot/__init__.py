from binance.api import API


class Spot(API):
    def __init__(self, api_key=None, api_secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.binance.com"
        super().__init__(api_key, api_secret, **kwargs)

    # MARKETS
    from binance.spot._market import ping
    from binance.spot._market import time
    from binance.spot._market import exchange_info
    from binance.spot._market import depth
    from binance.spot._market import trades
    from binance.spot._market import historical_trades
    from binance.spot._market import agg_trades
    from binance.spot._market import klines
    from binance.spot._market import ui_klines
    from binance.spot._market import avg_price
    from binance.spot._market import ticker_24hr
    from binance.spot._market import ticker_price
    from binance.spot._market import book_ticker
    from binance.spot._market import rolling_window_ticker

    # ACCOUNT (including orders and trades)
    from binance.spot._trade import new_order_test
    from binance.spot._trade import new_order
    from binance.spot._trade import cancel_order
    from binance.spot._trade import cancel_open_orders
    from binance.spot._trade import get_order
    from binance.spot._trade import cancel_and_replace
    from binance.spot._trade import get_open_orders
    from binance.spot._trade import get_orders
    from binance.spot._trade import new_oco_order
    from binance.spot._trade import cancel_oco_order
    from binance.spot._trade import get_oco_order
    from binance.spot._trade import get_oco_orders
    from binance.spot._trade import get_oco_open_orders
    from binance.spot._trade import account
    from binance.spot._trade import my_trades
    from binance.spot._trade import get_order_rate_limit

    # STREAMS
    from binance.spot._data_stream import new_listen_key
    from binance.spot._data_stream import renew_listen_key
    from binance.spot._data_stream import close_listen_key
    from binance.spot._data_stream import new_margin_listen_key
    from binance.spot._data_stream import renew_margin_listen_key
    from binance.spot._data_stream import close_margin_listen_key
    from binance.spot._data_stream import new_isolated_margin_listen_key
    from binance.spot._data_stream import renew_isolated_margin_listen_key
    from binance.spot._data_stream import close_isolated_margin_listen_key

    # MARGIN
    from binance.spot._margin import margin_transfer
    from binance.spot._margin import margin_borrow
    from binance.spot._margin import margin_repay
    from binance.spot._margin import margin_asset
    from binance.spot._margin import margin_pair
    from binance.spot._margin import margin_all_assets
    from binance.spot._margin import margin_all_pairs
    from binance.spot._margin import margin_pair_index
    from binance.spot._margin import new_margin_order
    from binance.spot._margin import cancel_margin_order
    from binance.spot._margin import margin_transfer_history
    from binance.spot._margin import margin_load_record
    from binance.spot._margin import margin_repay_record
    from binance.spot._margin import margin_interest_history
    from binance.spot._margin import margin_force_liquidation_record
    from binance.spot._margin import margin_account
    from binance.spot._margin import margin_order
    from binance.spot._margin import margin_open_orders
    from binance.spot._margin import margin_open_orders_cancellation
    from binance.spot._margin import margin_all_orders
    from binance.spot._margin import margin_my_trades
    from binance.spot._margin import margin_max_borrowable
    from binance.spot._margin import margin_max_transferable
    from binance.spot._margin import isolated_margin_transfer
    from binance.spot._margin import isolated_margin_transfer_history
    from binance.spot._margin import isolated_margin_account
    from binance.spot._margin import isolated_margin_pair
    from binance.spot._margin import isolated_margin_all_pairs
    from binance.spot._margin import toggle_bnbBurn
    from binance.spot._margin import bnbBurn_status
    from binance.spot._margin import margin_interest_rate_history
    from binance.spot._margin import new_margin_oco_order
    from binance.spot._margin import cancel_margin_oco_order
    from binance.spot._margin import get_margin_oco_order
    from binance.spot._margin import get_margin_oco_orders
    from binance.spot._margin import get_margin_open_oco_orders
    from binance.spot._margin import cancel_isolated_margin_account
    from binance.spot._margin import enable_isolated_margin_account
    from binance.spot._margin import isolated_margin_account_limit
    from binance.spot._margin import margin_fee
    from binance.spot._margin import isolated_margin_fee
    from binance.spot._margin import isolated_margin_tier
    from binance.spot._margin import margin_order_usage
    from binance.spot._margin import margin_dust_log
    from binance.spot._margin import summary_of_margin_account

    # SAVINGS
    from binance.spot._savings import savings_flexible_products
    from binance.spot._savings import savings_flexible_user_left_quota
    from binance.spot._savings import savings_purchase_flexible_product
    from binance.spot._savings import savings_flexible_user_redemption_quota
    from binance.spot._savings import savings_flexible_redeem
    from binance.spot._savings import savings_flexible_product_position
    from binance.spot._savings import savings_project_list
    from binance.spot._savings import savings_purchase_project
    from binance.spot._savings import savings_project_position
    from binance.spot._savings import savings_account
    from binance.spot._savings import savings_purchase_record
    from binance.spot._savings import savings_redemption_record
    from binance.spot._savings import savings_interest_history
    from binance.spot._savings import savings_change_position

    # Staking
    from binance.spot._staking import staking_product_list
    from binance.spot._staking import staking_purchase_product
    from binance.spot._staking import staking_redeem_product
    from binance.spot._staking import staking_product_position
    from binance.spot._staking import staking_history
    from binance.spot._staking import staking_set_auto_staking
    from binance.spot._staking import staking_product_quota

    # WALLET
    from binance.spot._wallet import system_status
    from binance.spot._wallet import coin_info
    from binance.spot._wallet import account_snapshot
    from binance.spot._wallet import disable_fast_withdraw
    from binance.spot._wallet import enable_fast_withdraw
    from binance.spot._wallet import withdraw
    from binance.spot._wallet import deposit_history
    from binance.spot._wallet import withdraw_history
    from binance.spot._wallet import deposit_address
    from binance.spot._wallet import account_status
    from binance.spot._wallet import api_trading_status
    from binance.spot._wallet import dust_log
    from binance.spot._wallet import user_universal_transfer
    from binance.spot._wallet import user_universal_transfer_history
    from binance.spot._wallet import transfer_dust
    from binance.spot._wallet import asset_dividend_record
    from binance.spot._wallet import asset_detail
    from binance.spot._wallet import trade_fee
    from binance.spot._wallet import funding_wallet
    from binance.spot._wallet import user_asset
    from binance.spot._wallet import api_key_permissions
    from binance.spot._wallet import bnb_convertible_assets
    from binance.spot._wallet import convertible_coins
    from binance.spot._wallet import toggle_auto_convertion
    from binance.spot._wallet import cloud_mining_trans_history
    from binance.spot._wallet import convert_transfer
    from binance.spot._wallet import convert_history

    # MINING
    from binance.spot._mining import mining_algo_list
    from binance.spot._mining import mining_coin_list
    from binance.spot._mining import mining_worker
    from binance.spot._mining import mining_worker_list
    from binance.spot._mining import mining_earnings_list
    from binance.spot._mining import mining_bonus_list
    from binance.spot._mining import mining_statistics_list
    from binance.spot._mining import mining_account_list
    from binance.spot._mining import mining_hashrate_resale_request
    from binance.spot._mining import mining_hashrate_resale_cancellation
    from binance.spot._mining import mining_hashrate_resale_list
    from binance.spot._mining import mining_hashrate_resale_details
    from binance.spot._mining import mining_account_earning

    # SUB-ACCOUNT
    from binance.spot._sub_account import sub_account_create
    from binance.spot._sub_account import sub_account_list
    from binance.spot._sub_account import sub_account_assets
    from binance.spot._sub_account import sub_account_deposit_address
    from binance.spot._sub_account import sub_account_deposit_history
    from binance.spot._sub_account import sub_account_status
    from binance.spot._sub_account import sub_account_enable_margin
    from binance.spot._sub_account import sub_account_margin_account
    from binance.spot._sub_account import sub_account_margin_account_summary
    from binance.spot._sub_account import sub_account_enable_futures
    from binance.spot._sub_account import sub_account_futures_transfer
    from binance.spot._sub_account import sub_account_margin_transfer
    from binance.spot._sub_account import sub_account_transfer_to_sub
    from binance.spot._sub_account import sub_account_transfer_to_master
    from binance.spot._sub_account import sub_account_transfer_sub_account_history
    from binance.spot._sub_account import sub_account_futures_asset_transfer_history
    from binance.spot._sub_account import sub_account_futures_asset_transfer
    from binance.spot._sub_account import sub_account_spot_summary
    from binance.spot._sub_account import sub_account_universal_transfer
    from binance.spot._sub_account import sub_account_universal_transfer_history
    from binance.spot._sub_account import sub_account_futures_account
    from binance.spot._sub_account import sub_account_futures_account_summary
    from binance.spot._sub_account import sub_account_futures_position_risk
    from binance.spot._sub_account import sub_account_spot_transfer_history
    from binance.spot._sub_account import sub_account_enable_leverage_token
    from binance.spot._sub_account import managed_sub_account_deposit
    from binance.spot._sub_account import managed_sub_account_assets
    from binance.spot._sub_account import managed_sub_account_withdraw
    from binance.spot._sub_account import sub_account_api_toggle_ip_restriction
    from binance.spot._sub_account import sub_account_api_add_ip
    from binance.spot._sub_account import sub_account_api_get_ip_restriction
    from binance.spot._sub_account import sub_account_api_delete_ip
    from binance.spot._sub_account import managed_sub_account_get_snapshot
    from binance.spot._sub_account import managed_sub_account_investor_trans_log
    from binance.spot._sub_account import managed_sub_account_trading_trans_log

    # FUTURES
    from binance.spot._futures import futures_transfer
    from binance.spot._futures import futures_transfer_history
    from binance.spot._futures import futures_loan_borrow_history
    from binance.spot._futures import futures_loan_repay_history
    from binance.spot._futures import futures_loan_wallet
    from binance.spot._futures import futures_loan_adjust_collateral_history
    from binance.spot._futures import futures_loan_liquidation_history
    from binance.spot._futures import futures_loan_interest_history

    # BLVTs
    from binance.spot._blvt import blvt_info
    from binance.spot._blvt import subscribe_blvt
    from binance.spot._blvt import subscription_record
    from binance.spot._blvt import redeem_blvt
    from binance.spot._blvt import redemption_record
    from binance.spot._blvt import user_limit_info

    # BSwap
    from binance.spot._bswap import bswap_pools
    from binance.spot._bswap import bswap_liquidity
    from binance.spot._bswap import bswap_liquidity_add
    from binance.spot._bswap import bswap_liquidity_remove
    from binance.spot._bswap import bswap_liquidity_operation_record
    from binance.spot._bswap import bswap_request_quote
    from binance.spot._bswap import bswap_swap
    from binance.spot._bswap import bswap_swap_history
    from binance.spot._bswap import bswap_pool_configure
    from binance.spot._bswap import bswap_add_liquidity_preview
    from binance.spot._bswap import bswap_remove_liquidity_preview
    from binance.spot._bswap import bswap_unclaimed_rewards
    from binance.spot._bswap import bswap_claim_rewards
    from binance.spot._bswap import bswap_claimed_rewards

    # FIAT
    from binance.spot._fiat import fiat_order_history
    from binance.spot._fiat import fiat_payment_history

    # C2C
    from binance.spot._c2c import c2c_trade_history

    # LOANS
    from binance.spot._loan import loan_history
    from binance.spot._loan import loan_borrow
    from binance.spot._loan import loan_borrow_history
    from binance.spot._loan import loan_ongoing_orders
    from binance.spot._loan import loan_repay
    from binance.spot._loan import loan_repay_history
    from binance.spot._loan import loan_adjust_ltv
    from binance.spot._loan import loan_adjust_ltv_history
    from binance.spot._loan import loan_vip_ongoing_orders
    from binance.spot._loan import loan_vip_repay
    from binance.spot._loan import loan_vip_repay_history
    from binance.spot._loan import loan_vip_collateral_account
    from binance.spot._loan import loan_loanable_data
    from binance.spot._loan import loan_collateral_data
    from binance.spot._loan import loan_collateral_rate
    from binance.spot._loan import loan_customize_margin_call

    # PAY
    from binance.spot._pay import pay_history

    # CONVERT
    from binance.spot._convert import convert_trade_history

    # REBATE
    from binance.spot._rebate import rebate_spot_history

    # NFT
    from binance.spot._nft import nft_transaction_history
    from binance.spot._nft import nft_deposit_history
    from binance.spot._nft import nft_withdraw_history
    from binance.spot._nft import nft_asset

    # Gift Card (Binance Code in the API documentation)
    from binance.spot._gift_card import gift_card_create_code
    from binance.spot._gift_card import gift_card_redeem_code
    from binance.spot._gift_card import gift_card_verify_code
    from binance.spot._gift_card import gift_card_rsa_public_key
    from binance.spot._gift_card import gift_card_buy_code
    from binance.spot._gift_card import gift_card_token_limit

    # Portfolio Margin
    from binance.spot._portfolio_margin import portfolio_margin_account
    from binance.spot._portfolio_margin import portfolio_margin_collateral_rate
    from binance.spot._portfolio_margin import portfolio_margin_bankruptcy_loan_amount
    from binance.spot._portfolio_margin import portfolio_margin_bankruptcy_loan_repay
