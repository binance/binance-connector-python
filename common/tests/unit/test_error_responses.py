import unittest
from unittest.mock import Mock, patch

import requests

from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import BadRequestError, ServerError, TooManyRequestsError
from binance_common.utils import send_request


def response(status, body, content_type="application/json", headers=None):
    result = requests.Response()
    result.status_code = status
    result._content = body
    result.headers["Content-Type"] = content_type
    result.headers.update(headers or {})
    return result


class ErrorResponseTests(unittest.TestCase):
    def setUp(self):
        self.config = ConfigurationRestAPI(
            base_path="https://example.invalid", retries=1, backoff=0
        )
        self.session = Mock()

    def request(self, method="GET"):
        return send_request(self.session, self.config, method, "/test")

    def test_malformed_or_non_object_client_errors_keep_status_type(self):
        for body in (b"", b"{", b"[]", b"null", b'"error"', b"42"):
            with self.subTest(body=body):
                self.session.request.return_value = response(400, body)
                with self.assertRaises(BadRequestError) as error:
                    self.request()
                self.assertEqual(
                    error.exception.error_message, BadRequestError().error_message
                )

    def test_invalid_rate_limit_body_preserves_retry_after(self):
        self.session.request.return_value = response(
            429, b"{", headers={"Retry-After": "30"}
        )
        with self.assertRaises(TooManyRequestsError) as error:
            self.request()
        self.assertEqual(error.exception.retry_after, 30)
        self.session.request.assert_called_once()

    @patch("binance_common.utils.time.sleep")
    def test_malformed_server_error_still_retries_get(self, sleep):
        self.session.request.side_effect = [
            response(503, b"{"),
            response(200, b'{"ok":true}'),
        ]
        self.assertEqual(self.request().data(), {"ok": True})
        self.assertEqual(self.session.request.call_count, 2)
        sleep.assert_called_once()

    @patch("binance_common.utils.time.sleep")
    def test_malformed_server_error_does_not_retry_post(self, sleep):
        self.session.request.return_value = response(503, b"{")
        with self.assertRaises(ServerError) as error:
            self.request("POST")
        self.assertEqual(error.exception.status_code, 503)
        self.session.request.assert_called_once()
        sleep.assert_not_called()

    @patch("binance_common.utils.time.sleep")
    def test_non_retriable_server_error_is_not_retried(self, sleep):
        self.session.request.return_value = response(501, b"{")
        with self.assertRaises(ServerError) as error:
            self.request()
        self.assertEqual(error.exception.status_code, 501)
        self.session.request.assert_called_once()
        sleep.assert_not_called()

    @patch("binance_common.utils.time.sleep")
    def test_exhausted_retries_raise_server_error(self, sleep):
        self.session.request.return_value = response(503, b"{")
        with self.assertRaises(ServerError) as error:
            self.request()
        self.assertEqual(error.exception.status_code, 503)
        self.assertEqual(self.session.request.call_count, 2)
        sleep.assert_called_once()

    def test_valid_error_object_preserves_code_and_message(self):
        self.session.request.return_value = response(
            400, b'{"code":-1100,"msg":"bad parameter"}'
        )
        with self.assertRaises(BadRequestError) as error:
            self.request()
        self.assertEqual(error.exception.status_code, -1100)
        self.assertEqual(error.exception.error_message, "bad parameter")


if __name__ == "__main__":
    unittest.main()
