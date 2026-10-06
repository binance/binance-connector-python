"""Regression tests for issue #566: HTTP 5xx retries and retry count accounting."""

import json
import unittest
from unittest.mock import MagicMock, patch

import requests

from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import NetworkError, ServerError
from binance_common.utils import send_request


def _json_response(status_code: int, payload: dict) -> MagicMock:
    """Builds a `requests.Response`-like mock with JSON content."""
    response = MagicMock(spec=requests.Response)
    response.status_code = status_code
    response.headers = {"Content-Type": "application/json"}
    response.text = json.dumps(payload)
    response.json.return_value = payload
    return response


def _make_config(retries: int = 3) -> ConfigurationRestAPI:
    """Config with backoff=0 so retries do not sleep during tests."""
    return ConfigurationRestAPI(
        api_key="key",
        api_secret="secret",
        base_path="https://api.binance.com",
        retries=retries,
        backoff=0,
        timeout=1000,
    )


class TestRetryOnServerError(unittest.TestCase):
    """Issue #566: 5xx must be retried, with retries + 1 total attempts."""

    def setUp(self):
        self.session = MagicMock(spec=requests.Session)

    def test_retries_on_500_then_succeeds(self):
        """Three 500s followed by a 200 → exactly 4 requests, returns data."""
        self.session.request.side_effect = [
            _json_response(500, {"msg": "server error"}),
            _json_response(500, {"msg": "server error"}),
            _json_response(500, {"msg": "server error"}),
            _json_response(200, {"ok": True}),
        ]

        response = send_request(
            session=self.session,
            configuration=_make_config(retries=3),
            method="GET",
            path="/api/v3/ping",
        )

        self.assertEqual(self.session.request.call_count, 4)
        self.assertEqual(response.data(), {"ok": True})

    def test_retries_on_502_503_504(self):
        """All of [500, 502, 503, 504] are retriable."""
        for code in (500, 502, 503, 504):
            with self.subTest(code=code):
                self.session.reset_mock()
                self.session.request.side_effect = [
                    _json_response(code, {"msg": "transient"}),
                    _json_response(200, {"ok": True}),
                ]

                response = send_request(
                    session=self.session,
                    configuration=_make_config(retries=3),
                    method="GET",
                    path="/api/v3/ping",
                )

                self.assertEqual(self.session.request.call_count, 2)
                self.assertEqual(response.data(), {"ok": True})

    def test_exhausts_all_attempts_on_persistent_500(self):
        """Persistent 500 with retries=3 → exactly 4 attempts, then ServerError."""
        self.session.request.return_value = _json_response(500, {"msg": "down"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 4)

    def test_retries_zero_means_single_attempt(self):
        """retries=0 → only the initial attempt runs."""
        self.session.request.return_value = _json_response(500, {"msg": "down"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=0),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 1)


class TestNoRetryOnNonRetriableServerErrors(unittest.TestCase):
    """5xx outside [500, 502, 503, 504] and non-GET/DELETE must not retry."""

    def setUp(self):
        self.session = MagicMock(spec=requests.Session)

    def test_501_is_not_retried(self):
        self.session.request.return_value = _json_response(501, {"msg": "nope"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 1)

    def test_505_is_not_retried(self):
        self.session.request.return_value = _json_response(505, {"msg": "nope"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 1)

    def test_post_500_is_not_retried(self):
        """POST is not idempotent → no retry even on 500."""
        self.session.request.return_value = _json_response(500, {"msg": "down"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="POST",
                path="/api/v3/order",
                body={"symbol": "BTCUSDT"},
            )

        self.assertEqual(self.session.request.call_count, 1)

    def test_put_500_is_not_retried(self):
        self.session.request.return_value = _json_response(500, {"msg": "down"})

        with self.assertRaises(ServerError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="PUT",
                path="/api/v3/order",
                body={"symbol": "BTCUSDT"},
            )

        self.assertEqual(self.session.request.call_count, 1)


class TestRetryOnConnectionError(unittest.TestCase):
    """Off-by-one fix: retries=3 must produce 4 total attempts, not 3."""

    def setUp(self):
        self.session = MagicMock(spec=requests.Session)

    def test_connection_error_exhausts_all_attempts(self):
        self.session.request.side_effect = requests.ConnectionError("boom")

        with self.assertRaises(NetworkError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 4)

    def test_connection_error_then_success(self):
        self.session.request.side_effect = [
            requests.ConnectionError("boom"),
            _json_response(200, {"ok": True}),
        ]

        response = send_request(
            session=self.session,
            configuration=_make_config(retries=3),
            method="GET",
            path="/api/v3/ping",
        )

        self.assertEqual(self.session.request.call_count, 2)
        self.assertEqual(response.data(), {"ok": True})

    def test_connection_error_on_post_is_not_retried(self):
        """POST + ConnectionError → no retry (idempotency guard)."""
        self.session.request.side_effect = requests.ConnectionError("boom")

        with self.assertRaises(NetworkError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="POST",
                path="/api/v3/order",
                body={"symbol": "BTCUSDT"},
            )

        self.assertEqual(self.session.request.call_count, 1)


class TestNoRegressionOnHappyPath(unittest.TestCase):
    """Fix must not alter successful-request behavior."""

    def setUp(self):
        self.session = MagicMock(spec=requests.Session)

    def test_200_single_attempt(self):
        self.session.request.return_value = _json_response(200, {"ok": True})

        response = send_request(
            session=self.session,
            configuration=_make_config(retries=3),
            method="GET",
            path="/api/v3/ping",
        )

        self.assertEqual(self.session.request.call_count, 1)
        self.assertEqual(response.data(), {"ok": True})
        self.assertEqual(response.status, 200)

    def test_400_is_not_retried(self):
        """4xx (client errors) must never retry."""
        from binance_common.errors import BadRequestError

        self.session.request.return_value = _json_response(400, {"msg": "bad"})

        with self.assertRaises(BadRequestError):
            send_request(
                session=self.session,
                configuration=_make_config(retries=3),
                method="GET",
                path="/api/v3/ping",
            )

        self.assertEqual(self.session.request.call_count, 1)


if __name__ == "__main__":
    unittest.main()