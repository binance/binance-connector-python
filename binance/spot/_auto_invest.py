from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def get_target_asset_list(self, **kwargs):
    """Get target asset list (USER_DATA)

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/target-asset/list

    https://binance-docs.github.io/apidocs/spot/en/#get-target-asset-list-user_data

    Keyword Args:
        targetAsset (str)
        size (int, optional): Default:8 Max:100
        current (int, optional): Current querying page. Start from 1. Default:1
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/lending/auto-invest/target-asset/list"
    return self.sign_request("GET", url_path, kwargs)


def get_target_asset_roi_data(self, targetAsset: str, hisRoiType: str, **kwargs):
    """Get target asset ROI data (USER_DATA)

    ROI return list for target asset

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/target-asset/roi/list

    https://binance-docs.github.io/apidocs/spot/en/#get-target-asset-roi-data-user_data

    Args:
        targetAsset (str)
        hisRoiType (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[targetAsset, "targetAsset"], [hisRoiType, "hisRoiType"]]
    )

    params = {"targetAsset": targetAsset, "hisRoiType": hisRoiType, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/target-asset/roi/list"
    return self.sign_request("GET", url_path, params)


def query_all_source_asset_and_target_asset(self, **kwargs):
    """Query all source asset and target asset (USER_DATA)

    Query all source assets and target assets

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/all/asset

    https://binance-docs.github.io/apidocs/spot/en/#query-all-source-asset-and-target-asset-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/lending/auto-invest/all/asset"
    return self.sign_request("GET", url_path, {**kwargs})


def query_source_asset_list(self, usageType: str, **kwargs):
    """Query source asset list (USER_DATA)

    Query Source Asset to be used for investment

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/source-asset/list

    https://binance-docs.github.io/apidocs/spot/en/#query-source-asset-list-user_data

    Args:
        usageType (str)
    Keyword Args:
        targetAsset (array, optional)
        indexId (int, optional)
        flexibleAllowedToUse (boolean, optional)
        sourceType (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(usageType, "usageType")

    params = {"usageType": usageType, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/source-asset/list"
    return self.sign_request("GET", url_path, params)


def change_plan_status(self, planId: int, status: str, **kwargs):
    """Change Plan Status (TRADE)

    Change Plan Status

    Weight(IP): 1

    POST /sapi/v1/lending/auto-invest/plan/edit-status

    https://binance-docs.github.io/apidocs/spot/en/#change-plan-status-trade

    Args:
        planId (int)
        status (Status)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[planId, "planId"], [status, "status"]])

    params = {"planId": planId, "status": status, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/plan/edit-status"
    return self.sign_request("POST", url_path, params)


def get_list_of_plans(self, planType: str, **kwargs):
    """Get list of plans (USER_DATA)

    Query plan lists

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/plan/list

    https://binance-docs.github.io/apidocs/spot/en/#get-list-of-plans-user_data

    Args:
        planType (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(planType, "planType")

    params = {"planType": planType, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/plan/list"
    return self.sign_request("GET", url_path, params)


def query_holding_details_of_the_plan(self, **kwargs):
    """Query holding details of the plan (USER_DATA)

    Query holding details of the plan

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/plan/id

    https://binance-docs.github.io/apidocs/spot/en/#query-holding-details-of-the-plan-user_data

    Keyword Args:
        planId (int, optional)
        requestId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/lending/auto-invest/plan/id"
    return self.sign_request("GET", url_path, {**kwargs})


def query_subscription_transaction_history(self, **kwargs):
    """Query subscription transaction history (USER_DATA)

    Query subscription transaction history of a plan

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/history/list

    https://binance-docs.github.io/apidocs/spot/en/#query-subscription-transaction-history-user_data

    Keyword Args:
        planType (str, optional)
        planId (int, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        targetAsset (float, optional)
        size (int, optional): Default:10 Max:100
        current (int, optional): Current querying page. Start from 1. Default:1
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/sapi/v1/lending/auto-invest/history/list"
    return self.sign_request("GET", url_path, kwargs)


def query_index_details(self, indexId: int, **kwargs):
    """Query Index Details (USER_DATA)

    Query index details

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/index/info

    https://binance-docs.github.io/apidocs/spot/en/#query-index-details-user_data

    Args:
        indexId (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(indexId, "indexId")

    params = {"indexId": indexId, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/index/info"
    return self.sign_request("GET", url_path, params)


def query_index_linked_plan_position_details(self, indexId: int, **kwargs):
    """Query Index Linked Plan Position Details (USER_DATA)

    Details on users Index-Linked plan position details

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/index/user-summary

    https://binance-docs.github.io/apidocs/spot/en/#query-index-linked-plan-position-details-user_data

    Args:
        indexId (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(indexId, "indexId")

    params = {"indexId": indexId, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/index/user-summary"
    return self.sign_request("GET", url_path, params)


def one_time_transaction(
    self, sourceType: str, subscriptionAmount: float, sourceAsset: str, **kwargs
):
    """One Time Transaction (TRADE)

    One time transaction

    Weight(IP): 1

    POST /sapi/v1/lending/auto-invest/one-off

    https://binance-docs.github.io/apidocs/spot/en/#one-time-transaction-trade

    Args:
        sourceType (str)
        subscriptionAmount (float)
        sourceAsset (str)
    Keyword Args:
        requestId (str, optional)
        flexibleAllowedToUse (boolean, optional)
        planId (int, optional)
        indexId (int, optional)
        details (list, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [sourceType, "sourceType"],
            [subscriptionAmount, "subscriptionAmount"],
            [sourceAsset, "sourceAsset"],
        ]
    )

    params = {
        "sourceType": sourceType,
        "subscriptionAmount": subscriptionAmount,
        "sourceAsset": sourceAsset,
        **kwargs,
    }
    url_path = "/sapi/v1/lending/auto-invest/one-off"
    return self.sign_request("POST", url_path, params)


def query_one_time_transaction_status(self, transactionId: int, **kwargs):
    """Query One-Time Transaction Status (USER_DATA)

    Transaction status for one-time transaction

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/one-off/status

    https://binance-docs.github.io/apidocs/spot/en/#query-one-time-transaction-status-user_data

    Args:
        transactionId (int)
    Keyword Args:
        requestId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(transactionId, "transactionId")

    params = {"transactionId": transactionId, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/one-off/status"
    return self.sign_request("GET", url_path, params)


def index_linked_plan_redemption(
    self, indexId: int, redemptionPercentage: int, **kwargs
):
    """Index Linked Plan Redemption (TRADE)

    To redeem index-Linked plan holdings

    Weight(IP): 1

    POST /sapi/v1/lending/auto-invest/redeem

    https://binance-docs.github.io/apidocs/spot/en/#index-linked-plan-redemption-trade

    Args:
        indexId (int)
        redemptionPercentage (int)
    Keyword Args:
        requestId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [[indexId, "indexId"], [redemptionPercentage, "redemptionPercentage"]]
    )

    params = {
        "indexId": indexId,
        "redemptionPercentage": redemptionPercentage,
        **kwargs,
    }
    url_path = "/sapi/v1/lending/auto-invest/redeem"
    return self.sign_request("POST", url_path, params)


def get_index_linked_plan_redemption_history(self, requestId: int, **kwargs):
    """Index Linked Plan Redemption (USER_DATA)

    Get the history of Index Linked Plan Redemption transactions

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/redeem/history

    https://binance-docs.github.io/apidocs/spot/en/#index-linked-plan-redemption-user_data

    Args:
        requestId (int)
    Keyword Args:
        asset (str, optional)
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(requestId, "requestId")

    params = {"requestId": requestId, **kwargs}
    url_path = "/sapi/v1/lending/auto-invest/redeem/history"
    return self.sign_request("GET", url_path, params)


def index_linked_plan_rebalance_details(self, **kwargs):
    """Index Linked Plan Rebalance Details (USER_DATA)

    Get the history of Index Linked Plan Redemption transactions

    Max 30 day difference between startTime and endTime
    If no startTime and endTime, default to show past 30 day records

    Weight(IP): 1

    GET /sapi/v1/lending/auto-invest/rebalance/history

    https://binance-docs.github.io/apidocs/spot/en/#index-linked-plan-rebalance-details-user_data

    Keyword Args:
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/lending/auto-invest/rebalance/history"
    return self.sign_request("GET", url_path, {**kwargs})
