from binance.lib.utils import check_required_parameters


def my_converts(self, startTime, endTime, **kwargs):
    check_required_parameters(
        [
            [startTime, "startTime"],
            [endTime, "endTime"]
        ]
    )

    url_path = "/sapi/v1/convert/tradeFlow"
    payload = {"startTime": startTime, "endTime": endTime, **kwargs}
    return self.sign_request("GET", url_path, payload)
