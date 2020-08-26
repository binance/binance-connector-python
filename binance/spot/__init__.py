from binance.api import API


class Spot(API):

    def __init__(self, key=None, secret=None, **kwargs):
        if 'base_url' not in kwargs:
            kwargs['base_url'] = 'https://api.binance.com'
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.spot.apis import ping
    from binance.spot.apis import time
    from binance.spot.apis import exchange_info
    from binance.spot.apis import depth
    from binance.spot.apis import trades
    from binance.spot.apis import historical_trades
    from binance.spot.apis import agg_trades
    from binance.spot.apis import klines
    from binance.spot.apis import avg_price
    from binance.spot.apis import ticker_24hr
    from binance.spot.apis import ticker_price
    from binance.spot.apis import book_ticker

    # USER_DATA or TRADES
    from binance.spot.apis import new_order_test
    from binance.spot.apis import new_order
    from binance.spot.apis import cancel_order
    from binance.spot.apis import cancel_open_orders
    from binance.spot.apis import get_order
    from binance.spot.apis import get_open_orders
    from binance.spot.apis import get_orders
    from binance.spot.apis import new_oco_order
    from binance.spot.apis import cancel_oco_order
    from binance.spot.apis import get_oco_order
    from binance.spot.apis import get_oco_orders
    from binance.spot.apis import get_oco_open_orders
    from binance.spot.apis import account
    from binance.spot.apis import my_trades

    # STREAMS
    from binance.spot.data_stream import new_listen_key
    from binance.spot.data_stream import renew_listen_key
    from binance.spot.data_stream import close_listen_key
    from binance.spot.data_stream import new_margin_listen_key
    from binance.spot.data_stream import renew_margin_listen_key
    from binance.spot.data_stream import close_margin_listen_key

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
    from binance.spot.margin import margin_all_orders
    from binance.spot.margin import margin_my_trades
    from binance.spot.margin import margin_max_borrowable
    from binance.spot.margin import margin_max_transferable

    # SAVINGS
    from binance.spot.savings import savings_flexible_products
    from binance.spot.savings import savings_flexible_user_left_quota
    from binance.spot.savings import savings_purchase_flexible_product
    from binance.spot.savings import savings_flexible_user_redemption_quota
    from binance.spot.savings import savings_flexible_redeem
    from binance.spot.savings import savings_flexible_product_position
    from binance.spot.savings import savings_product_list
    from binance.spot.savings import savings_purchase_customized_project
    from binance.spot.savings import savings_customized_position
    from binance.spot.savings import savings_account
    from binance.spot.savings import savings_purchase_record
    from binance.spot.savings import savings_redemption_record
    from binance.spot.savings import savings_interest_history

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
    from binance.spot.wallet import transfer_dust
    from binance.spot.wallet import asset_dividen_record
    from binance.spot.wallet import asset_detail
    from binance.spot.wallet import trade_fee

    # MINGING
    from binance.spot.minging import minging_algo_list
    from binance.spot.minging import minging_coin_list
    from binance.spot.minging import minging_worker
    from binance.spot.minging import minging_worker_list
    from binance.spot.minging import minging_revenue_list
    from binance.spot.minging import minging_statistics_list
    from binance.spot.minging import minging_account_list

    # SUB-ACCOUNT
    from binance.spot.corporate import sub_account_list
    from binance.spot.corporate import sub_account_transfer_history
    from binance.spot.corporate import sub_account_transfer
    from binance.spot.corporate import sub_account_asset
    from binance.spot.corporate import sub_account_deposit_address
    from binance.spot.corporate import sub_account_deposit_history
    from binance.spot.corporate import sub_account_status
    from binance.spot.corporate import sub_account_enable_margin
    from binance.spot.corporate import sub_account_margin_account
    from binance.spot.corporate import sub_account_margin_account_summary
    from binance.spot.corporate import sub_account_enable_futures
    from binance.spot.corporate import sub_account_futures_account
    from binance.spot.corporate import sub_account_futures_account_summary
    from binance.spot.corporate import sub_account_futures_position_risk
    from binance.spot.corporate import sub_account_futures_transfer
    from binance.spot.corporate import sub_account_margin_transfer
    from binance.spot.corporate import sub_account_transfer_to_sub
    from binance.spot.corporate import sub_account_transfer_to_master
    from binance.spot.corporate import sub_account_transfer_sub_account_history
