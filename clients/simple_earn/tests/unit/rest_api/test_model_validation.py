from binance_sdk_simple_earn.rest_api.models.subscribe_locked_product_response import (
    SubscribeLockedProductResponse,
)
from binance_sdk_simple_earn.rest_api.models.get_locked_product_position_response import (
    GetLockedProductPositionResponse,
)


def test_subscribe_locked_product_response_numeric_and_str_position_id():
    # Numeric positionId from production API
    payload_num = {
        "purchaseId": 351129167,
        "positionId": 347608223,
        "success": True,
    }
    resp = SubscribeLockedProductResponse.model_validate(payload_num)
    assert resp.purchase_id == 351129167
    assert resp.position_id == 347608223
    assert resp.success is True

    # String positionId
    payload_str = {
        "purchaseId": 351129167,
        "positionId": "347608223",
        "success": True,
    }
    resp_str = SubscribeLockedProductResponse.model_validate(payload_str)
    assert resp_str.position_id == "347608223"


def test_get_locked_product_position_response_numeric_fields():
    row = {
        "positionId": 347608038,
        "projectId": "Bnb*120",
        "asset": "BNB",
        "amount": "0.05",
        "purchaseTime": 1783439066000,
        "duration": 120,
        "accrualDays": 0,
        "rewardAsset": "BNB",
        "rewardAmt": "0",
        "nextPay": "0.00000054",
        "nextPayDate": 1783555200000,
        "payPeriod": 1,
        "redeemAmountEarly": "0.05",
        "rewardsEndDate": 1793836800000,
        "deliverDate": 1793959200000,
        "redeemPeriod": 1,
        "canRedeemEarly": True,
        "canFastRedemption": True,
        "autoSubscribe": False,
        "type": "NORMAL",
        "status": "HOLDING",
        "canReStake": False,
        "redeemTo": "SPOT",
        "totalBoostRewardAmt": "0",
        "apy": "0.004",
    }
    resp = GetLockedProductPositionResponse.model_validate({"rows": [row], "total": 1})
    assert resp.total == 1
    assert len(resp.rows) == 1
    assert resp.rows[0].position_id == 347608038
    assert resp.rows[0].duration == 120
    assert resp.rows[0].accrual_days == 0
    assert resp.rows[0].pay_period == 1
    assert resp.rows[0].redeem_period == 1
