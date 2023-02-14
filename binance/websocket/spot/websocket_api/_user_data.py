from binance.lib.utils import get_uuid


def user_data_start(self, id=None):
    """Start user data stream (USER_STREAM)

    Args:
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
            "method": "userDataStream.start",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
            "status": 200,
            "result": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"
            },
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }


    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.start",
        "params": {"apiKey": self.api_key},
    }

    self.send(payload)


def user_data_ping(self, listenKey: str, id=None):
    """Keepalive a user data stream to prevent a time out.

    Args:
        listenKey (str): The listen key from the user data stream
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "815d5fce-0880-4287-a567-80badf004c74",
            "method": "userDataStream.ping",
            "params": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "815d5fce-0880-4287-a567-80badf004c74",
            "status": 200,
            "response": {},
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }


    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.ping",
        "params": {"apiKey": self.api_key, "listenKey": listenKey},
    }

    self.send(payload)


def user_data_stop(self, listenKey: str, id=None):
    """Stop user data stream

    Args:
        listenKey (str): The listen key from the user data stream
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "819e1b1b-8c06-485b-a13e-131326c69599",
            "method": "userDataStream.stop",
            "params": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "819e1b1b-8c06-485b-a13e-131326c69599",
            "status": 200,
            "response": {},
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }

    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.stop",
        "params": {"apiKey": self.api_key, "listenKey": listenKey},
    }

    self.send(payload)
