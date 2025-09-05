import re
import time
import unittest
import hmac
import hashlib
import json
from pydantic import BaseModel
import requests

from base64 import b64decode, b64encode
from collections import OrderedDict
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15, eddsa
from types import SimpleNamespace
from typing import ClassVar, List, Optional, Union
from unittest.mock import Mock, patch
from urllib.parse import urlencode

from binance_common.constants import TimeUnit
from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import (
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    RateLimitBanError,
    TooManyRequestsError,
    ServerError,
    NetworkError,
)
from binance_common.models import RateLimit, WebsocketApiOptions
from binance_common.utils import (
    hmac_hashing,
    cleanNoneValue,
    get_timestamp,
    encoded_string,
    is_one_of_model,
    get_uuid,
    validate_time_unit,
    get_signature,
    should_retry_request,
    send_request,
    parse_rate_limit_headers,
    parse_proxies,
    ws_streams_placeholder,
    parse_ws_rate_limit_headers,
    normalize_query_values,
    ws_api_payload,
    websocket_api_signature,
    get_validator_field_map,
    resolve_model_from_event,
    parse_user_event,
)
from binance_common.headers import sanitize_header_value, parse_custom_headers
from binance_common.signature import Signers


class TestHmacHashing(unittest.TestCase):
    def test_valid_hmac_hashing(self):
        api_secret = "mysecretkey"
        payload = "testpayload"
        expected_hash = hmac.new(
            api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        self.assertEqual(hmac_hashing(api_secret, payload), expected_hash)

    def test_empty_payload(self):
        api_secret = "mysecretkey"
        payload = ""
        expected_hash = hmac.new(
            api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        self.assertEqual(hmac_hashing(api_secret, payload), expected_hash)

    def test_empty_api_secret(self):
        api_secret = ""
        payload = "testpayload"
        expected_hash = hmac.new(
            api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        self.assertEqual(hmac_hashing(api_secret, payload), expected_hash)

    def test_both_empty(self):
        api_secret = ""
        payload = ""
        expected_hash = hmac.new(
            api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        self.assertEqual(hmac_hashing(api_secret, payload), expected_hash)

    def test_different_inputs(self):
        api_secret_1 = "key1"
        api_secret_2 = "key2"
        payload_1 = "data1"
        payload_2 = "data2"
        self.assertNotEqual(
            hmac_hashing(api_secret_1, payload_1), hmac_hashing(api_secret_2, payload_2)
        )
        self.assertNotEqual(
            hmac_hashing(api_secret_1, payload_1), hmac_hashing(api_secret_1, payload_2)
        )
        self.assertNotEqual(
            hmac_hashing(api_secret_1, payload_1), hmac_hashing(api_secret_2, payload_1)
        )


class TestRsaSignature(unittest.TestCase):
    def test_valid_rsa_signature(self):
        private_key = RSA.generate(2048)
        private_pem = private_key.export_key().decode("utf-8")
        payload = "testpayload"

        config = Mock(private_key=private_pem, api_secret=None)
        signer = Signers.get_signer(private_pem)

        signature = get_signature(config, payload, signer=signer)

        public_key = private_key.publickey()
        digest = SHA256.new(payload.encode("utf-8"))
        decoded_signature = b64decode(signature)

        try:
            pkcs1_15.new(public_key).verify(digest, decoded_signature)
            verified = True
        except (ValueError, TypeError):
            verified = False

        self.assertTrue(verified)

    def test_invalid_rsa_signature(self):
        private_key = RSA.generate(2048)
        another_private_key = RSA.generate(2048)
        private_pem = private_key.export_key().decode("utf-8")
        payload = "testpayload"

        config = Mock(private_key=private_pem, api_secret=None)
        signer = Signers.get_signer(private_pem)

        signature = get_signature(config, payload, signer=signer)

        wrong_public_key = another_private_key.publickey()
        digest = SHA256.new(payload.encode("utf-8"))
        decoded_signature = b64decode(signature)

        with self.assertRaises(ValueError):
            pkcs1_15.new(wrong_public_key).verify(digest, decoded_signature)


class TestEd25519Signature(unittest.TestCase):
    def test_valid_ed25519_signature(self):
        private_key = ECC.generate(curve="ed25519")
        private_pem = private_key.export_key(format="PEM")
        payload = "testpayload"

        config = Mock(private_key=private_pem, api_secret=None)
        signer = Signers.get_signer(private_pem)

        signature = get_signature(config, payload, signer)

        public_key = private_key.public_key()
        decoded_signature = b64decode(signature)
        verifier = eddsa.new(public_key, "rfc8032")

        try:
            verifier.verify(payload.encode("utf-8"), decoded_signature)
            verified = True
        except ValueError:
            verified = False

        self.assertTrue(verified)

    def test_invalid_ed25519_signature(self):
        private_key = ECC.generate(curve="ed25519")
        another_private_key = ECC.generate(curve="ed25519")
        private_pem = private_key.export_key(format="PEM")
        payload = "testpayload"

        config = Mock(private_key=private_pem, api_secret=None)
        signer = Signers.get_signer(private_pem)

        signature = get_signature(config, payload, signer)

        public_key = another_private_key.public_key()
        decoded_signature = b64decode(signature)
        verifier = eddsa.new(public_key, "rfc8032")

        with self.assertRaises(ValueError):
            verifier.verify(payload.encode("utf-8"), decoded_signature)


class TestCleanNoneValue(unittest.TestCase):
    def test_remove_none_values(self):
        input_dict = {"a": 1, "b": None, "c": 3, "d": None}
        expected_output = {"a": 1, "c": 3}
        self.assertEqual(cleanNoneValue(input_dict), expected_output)

    def test_all_none_values(self):
        input_dict = {"a": None, "b": None, "c": None}
        expected_output = {}
        self.assertEqual(cleanNoneValue(input_dict), expected_output)

    def test_no_none_values(self):
        input_dict = {"a": 1, "b": 2, "c": 3}
        expected_output = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(cleanNoneValue(input_dict), expected_output)

    def test_empty_dictionary(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(cleanNoneValue(input_dict), expected_output)

    def test_mixed_types(self):
        input_dict = {"a": 0, "b": False, "c": None, "d": "", "e": [], "f": {}}
        expected_output = {"a": 0, "b": False, "d": "", "e": [], "f": {}}
        self.assertEqual(cleanNoneValue(input_dict), expected_output)


class TestGetTimestamp(unittest.TestCase):
    def test_timestamp_is_integer(self):
        timestamp = get_timestamp()
        self.assertIsInstance(timestamp, int)

    def test_timestamp_is_current(self):
        lower_bound = int(time.time() * 1000)
        timestamp = get_timestamp()
        upper_bound = int(time.time() * 1000)

        self.assertGreaterEqual(timestamp, lower_bound)
        self.assertLessEqual(timestamp, upper_bound)

    def test_timestamps_are_increasing(self):
        timestamp1 = get_timestamp()
        time.sleep(0.01)
        timestamp2 = get_timestamp()

        self.assertGreater(timestamp2, timestamp1)


class TestEncodedString(unittest.TestCase):
    def test_encode_regular_string(self):
        query = {"message": "hello world"}
        expected_output = urlencode(query, doseq=True)
        self.assertEqual(encoded_string(query), expected_output)

    def test_encode_string_with_special_characters(self):
        query = {"email": "test@example.com"}
        expected_output = urlencode(query, doseq=True)
        self.assertEqual(encoded_string(query), expected_output)

    def test_encode_empty_string(self):
        query = {}
        expected_output = urlencode(query, doseq=True)
        self.assertEqual(encoded_string(query), expected_output)

    def test_encode_string_with_multiple_at_symbols(self):
        query = {"user": "test@example.com", "admin": "admin@domain.com"}
        expected_output = urlencode(query, doseq=True)
        self.assertEqual(encoded_string(query), expected_output)

    def test_encode_string_with_array(self):
        query = {"ids": [1, 2, 3]}
        expected_output = "ids=%5B1%2C2%2C3%5D"
        self.assertEqual(encoded_string(query), expected_output)

    def test_encode_with_class_instances_in_list(self):
        class Dummy:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        dummy_instance = Dummy("value1", 123)
        query = {"items": [dummy_instance]}

        expected_value = urlencode({
            "items": json.dumps([{"a": "value1", "b": 123}], separators=(",", ":"))
        }, doseq=True)

        self.assertEqual(encoded_string(query), expected_value)


class TestIsOneOfModel(unittest.TestCase):

    class DummyOneOf(BaseModel):
        a: int
        b: str
        actual_instance_must_validate_oneof: ClassVar[bool] = True
        def is_oneof_model() -> bool:
            return True

    class DummyNotOneOf(BaseModel):
        x: float

    def test_is_one_of_model_valid(self):
        self.assertTrue(is_one_of_model(self.DummyOneOf))

    def test_is_one_of_model_invalid(self):
        self.assertFalse(is_one_of_model(self.DummyNotOneOf))

class TestGetUUID(unittest.TestCase):
    def test_uuid_is_string(self):
        generated_uuid = get_uuid()
        self.assertIsInstance(generated_uuid, str)

    def test_uuid_is_valid_format(self):
        generated_uuid = get_uuid()
        uuid_regex = re.compile(
            r"^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$",
            re.IGNORECASE,
        )
        self.assertRegex(generated_uuid, uuid_regex)

    def test_uuid_is_unique(self):
        uuid1 = get_uuid()
        uuid2 = get_uuid()
        self.assertNotEqual(uuid1, uuid2)


class TestValidateTimeUnit(unittest.TestCase):
    def test_valid_time_units(self):
        valid_units = [
            TimeUnit.MICROSECOND.value,
            TimeUnit.microsecond.value,
            TimeUnit.MILLISECOND.value,
            TimeUnit.millisecond.value,
        ]
        for unit in valid_units:
            with self.subTest(unit=unit):
                self.assertEqual(validate_time_unit(unit), unit)

    def test_invalid_time_unit(self):
        with self.assertRaises(ValueError):
            validate_time_unit("weeks")

        with self.assertRaises(ValueError):
            validate_time_unit("random_unit")

    def test_none_time_unit(self):
        self.assertIsNone(validate_time_unit(None))


class TestGetSignature(unittest.TestCase):
    def setUp(self):
        self.hmac_secret = "mysecret"

        self.hmac_config = Mock(
            api_secret=self.hmac_secret, private_key=None, private_key_algo=None
        )

        self.rsa_key = RSA.generate(2048)
        self.rsa_config = Mock(
            api_secret=None,
            private_key=self.rsa_key.export_key().decode("utf-8"),
            private_key_passphrase=None,
        )

        self.ed25519_key = ECC.generate(curve="ed25519")
        self.ed25519_config = Mock(
            api_secret=None,
            private_key=self.ed25519_key.export_key(format="PEM"),
            private_key_passphrase=None,
        )

        self.invalid_algo_config = Mock(
            api_secret=None,
            private_key="some_private_key",
            private_key_passphrase=None,
        )

        self.missing_keys_config = Mock(
            api_secret=None, private_key=None
        )

    def test_hmac_signature(self):
        payload = {"key": "value"}
        payload_str = json.dumps(payload, separators=(",", ":"))
        expected_signature = hmac_hashing(self.hmac_secret, payload_str)
        self.assertEqual(
            get_signature(self.hmac_config, payload_str), expected_signature
        )

    def test_rsa_signature(self):
        payload = {"key": "value"}
        payload_str = json.dumps(payload, separators=(",", ":"))
        signer = Signers.get_signer(self.rsa_key.export_key().decode("utf-8"))
        expected_signature = b64encode(
            signer.sign(SHA256.new(payload_str.encode("utf-8")))
        ).decode("utf-8")
        self.assertEqual(
            get_signature(self.rsa_config, payload_str, signer), expected_signature
        )

    def test_ed25519_signature(self):
        payload = {"key": "value"}
        payload_str = json.dumps(payload, separators=(",", ":"))
        signer = Signers.get_signer(self.ed25519_key.export_key(format="PEM"))
        expected_signature = b64encode(
            signer.sign(payload_str.encode("utf-8"))
        ).decode("utf-8")
        self.assertEqual(
            get_signature(self.ed25519_config, payload_str, signer), expected_signature
        )

    def test_invalid_private_key_algo(self):
        with self.assertRaises(ValueError) as context:
            Signers.get_signer(self.invalid_algo_config.private_key)
        self.assertEqual(
            str(context.exception),
            "Unsupported or invalid private key format. Private key must be either 'RSA' or 'ED25519'",
        )

    def test_missing_keys(self):
        payload = {"key": "value"}
        payload_str = json.dumps(payload, separators=(",", ":"))
        with self.assertRaises(ValueError) as context:
            get_signature(self.missing_keys_config, payload_str)
        self.assertEqual(
            str(context.exception),
            "Either 'api_secret' or 'private_key' must be provided for signed requests.",
        )


class TestShouldRetryRequest(unittest.TestCase):
    def test_retry_on_retriable_status_code(self):
        error = Mock(response=Mock(status_code=500))
        self.assertTrue(should_retry_request(error, method="GET", retries_left=3))

        error.response.status_code = 502
        self.assertTrue(should_retry_request(error, method="DELETE", retries_left=2))

        error.response.status_code = 503
        self.assertTrue(should_retry_request(error, method="GET", retries_left=1))

        error.response.status_code = 504
        self.assertTrue(should_retry_request(error, method="DELETE", retries_left=1))

    def test_no_retry_on_non_retriable_status_code(self):
        error = Mock(response=Mock(status_code=400))
        self.assertFalse(should_retry_request(error, method="GET", retries_left=3))

        error.response.status_code = 401
        self.assertFalse(should_retry_request(error, method="DELETE", retries_left=2))

        error.response.status_code = 404
        self.assertFalse(should_retry_request(error, method="GET", retries_left=1))

        error.response.status_code = 200
        self.assertFalse(should_retry_request(error, method="DELETE", retries_left=1))

    def test_no_retry_on_non_retriable_method(self):
        error = Mock(response=Mock(status_code=500))
        self.assertFalse(should_retry_request(error, method="POST", retries_left=3))
        self.assertFalse(should_retry_request(error, method="PUT", retries_left=3))

    def test_no_retry_when_no_retries_left(self):
        error = Mock(response=Mock(status_code=500))
        self.assertFalse(should_retry_request(error, method="GET", retries_left=0))

        error.response.status_code = 503
        self.assertFalse(should_retry_request(error, method="DELETE", retries_left=-1))

    def test_retry_on_no_response_attribute(self):
        error = Mock(response=None)
        self.assertTrue(should_retry_request(error, method="GET", retries_left=3))

    def test_no_retry_when_method_is_none(self):
        error = Mock(response=Mock(status_code=500))
        self.assertFalse(should_retry_request(error, method=None, retries_left=3))

    def test_no_retry_when_retries_left_is_none(self):
        error = Mock(response=Mock(status_code=500))
        self.assertFalse(should_retry_request(error, method="GET", retries_left=None))


class TestSendRequest(unittest.TestCase):
    def setUp(self):
        self.session = Mock(spec=requests.Session)
        self.configuration = ConfigurationRestAPI(
            api_key="test_key",
            api_secret="test_secret",
            base_path="https://api.test.com",
            retries=3,
            backoff=1,
            timeout=5000,
            proxy=None,
            compression=False,
            https_agent=None,
            keep_alive=False,
        )
        self.method = "GET"
        self.path = "/test"
        self.url = f"{self.configuration.base_path}{self.path}"

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch("binance_common.utils.parse_rate_limit_headers", return_value=[])
    @patch("binance_common.utils.get_timestamp", return_value=1234567890)
    @patch("binance_common.utils.get_signature", return_value="signed_signature")
    def test_signed_request(
        self,
        mock_get_signature,
        mock_get_timestamp,
        mock_parse_rate_limits,
        mock_clean_none,
        mock_encoded_string,
    ):
        """Test signed request includes signature and timestamp."""
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = {"success": True}
        mock_response.text = json.dumps({"success": True})

        self.session.request.return_value = mock_response

        response = send_request(
            self.session,
            self.configuration,
            self.method,
            self.path,
            payload={"param": "value"},
            is_signed=True,
        )

        self.assertEqual(response.data(), {"success": True})
        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers, mock_response.headers)
        self.assertEqual(response.status, 200)

        self.session.request.assert_called_once()
        _, kwargs = self.session.request.call_args

        self.assertIn("timestamp", kwargs["params"])
        self.assertIn("signature", kwargs["params"])
        self.assertEqual(kwargs["params"]["timestamp"], 1234567890)
        self.assertEqual(kwargs["params"]["signature"], "signed_signature")

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch("binance_common.utils.parse_rate_limit_headers", return_value=[])
    def test_successful_request(
        self, mock_parse_rate_limits, mock_clean_none, mock_encoded_string
    ):
        """Test successful request (200 response)."""
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = {"success": True}
        mock_response.text = json.dumps({"success": True})

        self.session.request.return_value = mock_response

        response = send_request(
            self.session, self.configuration, self.method, self.path, {"param": "value"}
        )

        self.assertEqual(response.data(), {"success": True})
        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers, mock_response.headers)
        self.assertEqual(response.rate_limits, [])

        headers = self.configuration.base_headers
        headers["Connection"] = "close"

        self.session.request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params={"param": "value"},
            headers=headers,
            timeout=5,
            proxies=None,
        )

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch("binance_common.utils.parse_rate_limit_headers", return_value=[])
    def test_successful_request_empty_array_response(
        self, mock_parse_rate_limits, mock_clean_none, mock_encoded_string
    ):
        """Test successful request (200 response)."""
        mock_response = Mock(status_code=200)
        mock_response.json.return_value = []
        mock_response.text = json.dumps([])

        self.session.request.return_value = mock_response

        response = send_request(
            self.session, self.configuration, self.method, self.path, {"param": "value"}
        )

        self.assertEqual(response.data(), [])
        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers, mock_response.headers)
        self.assertEqual(response.rate_limits, [])

        headers = self.configuration.base_headers
        headers["Connection"] = "close"

        self.session.request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params={"param": "value"},
            headers=headers,
            timeout=5,
            proxies=None,
        )

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    def test_client_errors(self, mock_clean_none, mock_encoded_string):
        """Test 400-499 errors raising appropriate exceptions."""
        error_cases = {
            400: BadRequestError,
            401: UnauthorizedError,
            403: ForbiddenError,
            404: NotFoundError,
            418: RateLimitBanError,
            429: TooManyRequestsError,
        }

        for status, exception in error_cases.items():
            with self.subTest(status=status):
                mock_response = Mock(
                    status_code=status, headers={"Content-Type": "application/json"}
                )

                mock_response.json.return_value = {"msg": f"Error {status}"}
                self.session.request.return_value = mock_response

                with self.assertRaises(exception) as context:
                    send_request(
                        self.session, self.configuration, self.method, self.path, {}
                    )

                self.assertEqual(context.exception.error_message, f"Error {status}")

                mock_response.json.return_value = {}
                self.session.request.return_value = mock_response

                with self.assertRaises(exception) as context:
                    send_request(
                        self.session, self.configuration, self.method, self.path, {}
                    )

                self.assertEqual(
                    context.exception.error_message, exception().error_message
                )

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    def test_server_errors(self, mock_clean_none, mock_encoded_string):
        """Test 500-599 server errors raising ServerError."""
        for status in [500, 502, 503, 504]:
            with self.subTest(status=status):
                mock_response = Mock(status_code=status)
                mock_response.json.return_value = {"msg": "Server Error"}
                self.session.request.return_value = mock_response

                with self.assertRaises(ServerError) as context:
                    send_request(
                        self.session, self.configuration, self.method, self.path, {}
                    )

                self.assertEqual(str(context.exception), f"Server error: {status}")

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch(
        "binance_common.utils.should_retry_request",
        side_effect=lambda e, m, r: r > 0
        and (getattr(e, "response", None) is None or e.response.status_code != 500),
    )
    @patch("time.sleep", return_value=None)
    def test_network_error_with_retry(
        self, mock_sleep, mock_should_retry, mock_clean_none, mock_encoded_string
    ):
        """Test request retrying on network errors."""

        mock_response = Mock(status_code=500)
        self.session.request.side_effect = [
            requests.RequestException("Network Error"),
            mock_response,
        ]

        with self.assertRaises(ServerError):
            send_request(self.session, self.configuration, self.method, self.path, {})

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch("binance_common.utils.should_retry_request", return_value=False)
    def test_network_error_no_retry(
        self, mock_should_retry, mock_clean_none, mock_encoded_string
    ):
        """Test request failure when retry is not allowed."""
        self.session.request.side_effect = requests.RequestException("Network Error")

        with self.assertRaises(NetworkError) as context:
            send_request(self.session, self.configuration, self.method, self.path, {})

        self.assertEqual(str(context.exception), "Network error: Network Error")
        self.assertEqual(mock_should_retry.call_count, 1)

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    def test_correct_headers_and_proxies(self, mock_clean_none, mock_encoded_string):
        """Ensure correct headers and proxies are used in request."""
        self.configuration.proxy = {
            "protocol": "https",
            "host": "127.0.0.1",
            "port": 8080,
        }
        self.configuration.compression = True

        mock_response = Mock(status_code=200)
        mock_response.json.return_value = {"success": True}
        mock_response.headers = {"x-mbx-used-weight-1m": "10"}
        mock_response.text = json.dumps({"success": True})
        self.session.request.return_value = mock_response

        send_request(self.session, self.configuration, self.method, self.path, {})

        self.session.request.assert_called_once()
        _, kwargs = self.session.request.call_args

        self.assertEqual(kwargs["headers"]["Accept-Encoding"], "gzip, deflate, br")
        self.assertEqual(
            kwargs["proxies"],
            {"http": "https://127.0.0.1:8080", "https": "https://127.0.0.1:8080"},
        )

    @patch("binance_common.utils.encoded_string", side_effect=lambda x: x)
    @patch("binance_common.utils.cleanNoneValue", side_effect=lambda x: x)
    @patch("binance_common.utils.should_retry_request", return_value=False)
    def test_request_fails_after_retries(
        self, mock_should_retry, mock_clean_none, mock_encoded_string
    ):
        """Ensure request fails after max retries are exhausted."""
        self.configuration.retries = 2
        self.session.request.side_effect = requests.RequestException("Final Failure")

        with self.assertRaises(NetworkError) as context:
            send_request(self.session, self.configuration, self.method, self.path, {})

        self.assertEqual(str(context.exception), "Network error: Final Failure")


class TestParseRateLimitHeaders(unittest.TestCase):
    def test_parse_used_weight_header(self):
        """Test parsing 'x-mbx-used-weight-*' headers"""
        headers = {"x-mbx-used-weight-1m": "100"}

        expected_output: List[RateLimit] = [
            RateLimit(
                rateLimitType="REQUEST_WEIGHT",
                interval="MINUTE",
                intervalNum=1,
                count=100,
                retryAfter=None,
            )
        ]

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_order_count_header(self):
        """Test parsing 'x-mbx-order-count-*' headers"""
        headers = {"x-mbx-order-count-5s": "50"}

        expected_output: List[RateLimit] = [
            RateLimit(
                rateLimitType="ORDERS",
                interval="SECOND",
                intervalNum=5,
                count=50,
                retryAfter=None,
            )
        ]

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_multiple_headers(self):
        """Test parsing multiple rate limit headers"""
        headers = {
            "x-mbx-used-weight-1m": "100",
            "x-mbx-order-count-5s": "50",
            "x-mbx-used-weight-1h": "5000",
        }

        expected_output: List[RateLimit] = [
            RateLimit(
                rateLimitType="REQUEST_WEIGHT",
                interval="MINUTE",
                intervalNum=1,
                count=100,
                retryAfter=None,
            ),
            RateLimit(
                rateLimitType="ORDERS",
                interval="SECOND",
                intervalNum=5,
                count=50,
                retryAfter=None,
            ),
            RateLimit(
                rateLimitType="REQUEST_WEIGHT",
                interval="HOUR",
                intervalNum=1,
                count=5000,
                retryAfter=None,
            ),
        ]

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_retry_after_header(self):
        """Test parsing 'retry-after' header"""
        headers = {
            "x-mbx-used-weight-1m": "200",
            "retry-after": "10",
        }

        expected_output: List[RateLimit] = [
            RateLimit(
                rateLimitType="REQUEST_WEIGHT",
                interval="MINUTE",
                intervalNum=1,
                count=200,
                retryAfter=10,
            )
        ]

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_invalid_headers(self):
        """Test handling of malformed or irrelevant headers"""
        headers = {
            "x-mbx-used-weight-xyz": "200",
            "x-mbx-order-count-5y": "50",
            "some-other-header": "123",
        }

        expected_output: List[RateLimit] = []

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_empty_headers(self):
        """Test handling of empty headers"""
        headers = {}

        expected_output: List[RateLimit] = []

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)

    def test_parse_none_values(self):
        """Test handling of headers with None values"""
        headers = {
            "x-mbx-used-weight-1m": None,
            "x-mbx-order-count-1h": "100",
        }

        expected_output: List[RateLimit] = [
            RateLimit(
                rateLimitType="ORDERS",
                interval="HOUR",
                intervalNum=1,
                count=100,
                retryAfter=None,
            )
        ]

        self.assertEqual(parse_rate_limit_headers(headers), expected_output)


class TestParseProxies(unittest.TestCase):
    def test_parse_full_proxy_with_auth(self):
        """Test parsing a full proxy configuration with authentication"""
        proxy_config = {
            "protocol": "http",
            "host": "proxyserver.com",
            "port": 8080,
            "auth": {"username": "user", "password": "pass"},
        }

        expected_output = {
            "https": "http://user:pass@proxyserver.com:8080",
            "http": "http://user:pass@proxyserver.com:8080",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)

    def test_parse_proxy_without_auth(self):
        """Test parsing a proxy configuration without authentication"""
        proxy_config = {
            "protocol": "http",
            "host": "proxyserver.com",
            "port": 8080,
        }

        expected_output = {
            "https": "http://proxyserver.com:8080",
            "http": "http://proxyserver.com:8080",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)

    def test_parse_proxy_with_missing_protocol(self):
        """Test proxy configuration with missing protocol (defaults to https)"""
        proxy_config = {
            "host": "proxyserver.com",
            "port": 8080,
        }

        expected_output = {
            "https": "https://proxyserver.com:8080",
            "http": "https://proxyserver.com:8080",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)

    def test_parse_proxy_with_missing_host(self):
        """Test proxy configuration with missing host"""
        proxy_config = {
            "protocol": "http",
            "port": 8080,
        }

        expected_output = {
            "https": "http://:8080",
            "http": "http://:8080",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)

    def test_parse_proxy_with_missing_port(self):
        """Test proxy configuration with missing port"""
        proxy_config = {
            "protocol": "http",
            "host": "proxyserver.com",
        }

        expected_output = {
            "https": "http://proxyserver.com:",
            "http": "http://proxyserver.com:",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)

    def test_parse_proxy_none(self):
        """Test parsing a None proxy config (should return None)"""
        self.assertIsNone(parse_proxies(None))

    def test_parse_proxy_empty_dict(self):
        """Test parsing an empty dictionary (should return None)"""
        self.assertIsNone(parse_proxies({}))

    def test_parse_proxy_with_integer_port(self):
        """Test handling of integer port"""
        proxy_config = {
            "protocol": "http",
            "host": "proxyserver.com",
            "port": 8080,
        }

        expected_output = {
            "https": "http://proxyserver.com:8080",
            "http": "http://proxyserver.com:8080",
        }

        self.assertEqual(parse_proxies(proxy_config), expected_output)


class TestWsStreamsPlaceholder(unittest.TestCase):
    def test_replace_single_placeholder(self):
        stream = "<symbol>@depth"
        params = {"symbol": "BTCUSDT"}
        result = ws_streams_placeholder(stream, params)
        self.assertEqual(result, "btcusdt@depth")

    def test_replace_multiple_placeholders(self):
        stream = "<symbol>@depth<update_speed>"
        params = {"symbol": "BTCUSDT", "update_speed": "100ms"}
        result = ws_streams_placeholder(stream, params)
        self.assertEqual(result, "btcusdt@depth@100ms")

    def test_ignore_none_values(self):
        stream = "<symbol>@depth<update_speed>"
        params = {"symbol": "BTCUSDT", "update_speed": None}
        result = ws_streams_placeholder(stream, params)
        self.assertEqual(result, "btcusdt@depth")

    def test_format_with_dashes_and_case_insensitivity(self):
        stream = "<SYMBOL>@depth<update-speed>"
        params = {"symbol": "BTCUSDT", "update_speed": "100ms"}
        result = ws_streams_placeholder(stream, params)
        self.assertEqual(result, "btcusdt@depth@100ms")

    def test_placeholder_not_found_in_params(self):
        stream = "<symbol>@depth<missing>"
        params = {"symbol": "BTCUSDT"}
        result = ws_streams_placeholder(stream, params)
        self.assertEqual(result, "btcusdt@depth")


class TestParseWsRateLimitHeaders(unittest.TestCase):
    def test_parse_single_ratelimit_header(self):
        headers = [{
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 12
        }]
        result = parse_ws_rate_limit_headers(headers)
        self.assertEqual(len(result), 1)

        rl = result[0]
        self.assertEqual(rl.rateLimitType, "ORDERS")
        self.assertEqual(rl.interval, "SECOND")
        self.assertEqual(rl.intervalNum, 10)
        self.assertEqual(rl.limit, 50)
        self.assertEqual(rl.count, 12)

    def test_parse_multiple_ratelimit_headers(self):
        headers = [
            {
                "rateLimitType": "ORDERS",
                "interval": "SECOND",
                "intervalNum": 10,
                "limit": 50,
                "count": 12
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "DAY",
                "intervalNum": 1,
                "limit": 160000,
                "count": 4043
            },
            {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 6000,
                "count": 321
            }
        ]
        result = parse_ws_rate_limit_headers(headers)
        self.assertEqual(len(result), 3)

        self.assertEqual(result[0].rateLimitType, "ORDERS")
        self.assertEqual(result[1].interval, "DAY")
        self.assertEqual(result[2].limit, 6000)
        self.assertEqual(result[2].count, 321)

    def test_missing_optional_count_defaults_to_zero(self):
        headers = [{
            "rateLimitType": "ORDERS",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 100
        }]
        result = parse_ws_rate_limit_headers(headers)
        self.assertEqual(result[0].count, 0)


class TestNormalizeQueryValues(unittest.TestCase):
    def test_convert_single_boolean(self):
        parsed = {"test": ["true"]}
        result = normalize_query_values(parsed)
        self.assertEqual(result["test"], True)

    def test_convert_multiple_numbers(self):
        parsed = {"nums": ["1", "2", "3"]}
        result = normalize_query_values(parsed)
        self.assertEqual(result["nums"], [1, 2, 3])

    def test_convert_float_and_int(self):
        parsed = {"int": ["5"], "float": ["3.14"]}
        result = normalize_query_values(parsed)
        self.assertEqual(result["int"], 5)
        self.assertEqual(result["float"], 3.14)

    def test_expected_types_override(self):
        parsed = {"a": ["1", "2"]}
        expected_types = {"a": int}
        result = normalize_query_values(parsed, expected_types)
        self.assertEqual(result["a"], [1, 2])

    def test_string_value(self):
        parsed = {"text": ["hello"]}
        result = normalize_query_values(parsed)
        self.assertEqual(result["text"], "hello")

    def test_strip_whitespace_and_case(self):
        parsed = {"flag": ["  FaLsE  "]}
        result = normalize_query_values(parsed)
        self.assertEqual(result["flag"], False)

class TestSanitizeHeaderValue(unittest.TestCase):
    def test_returns_simple_string_unchanged(self):
        self.assertEqual(sanitize_header_value("foo-bar"), "foo-bar")

    def test_throws_on_string_containing_CR(self):
        with self.assertRaises(ValueError) as context:
            sanitize_header_value("bad\rvalue")
        self.assertEqual(
            str(context.exception),
            'Invalid header value (contains CR/LF): "bad\rvalue"',
        )

    def test_throws_on_string_containing_LF(self):
        with self.assertRaises(ValueError) as context:
            sanitize_header_value("bad\nvalue")
        self.assertEqual(
            str(context.exception),
            'Invalid header value (contains CR/LF): "bad\nvalue"',
        )

    def test_returns_array_of_strings_when_clean(self):
        arr: List[str] = ["one", "two", "three"]
        self.assertEqual([sanitize_header_value(v) for v in arr], arr)

    def test_throws_if_any_element_in_array_contains_CRLF(self):
        arr: List[str] = ["good", "bad\nvalue", "also-good"]
        with self.assertRaises(ValueError) as context:
            [sanitize_header_value(v) for v in arr]
        self.assertEqual(
            str(context.exception),
            'Invalid header value (contains CR/LF): "bad\nvalue"',
        )


class TestParseCustomHeaders(unittest.TestCase):
    def test_returns_empty_dict_when_input_is_empty_or_none(self):
        assert parse_custom_headers({}) == {}
        assert parse_custom_headers(None) == {}

    def test_keeps_a_single_safe_header(self):
        input_data = {"X-Test": "ok"}
        assert parse_custom_headers(input_data) == {"X-Test": "ok"}

    def test_trims_whitespace_around_header_names(self):
        input_data = {"  X-Trim  ": "value"}
        assert parse_custom_headers(input_data) == {"X-Trim": "value"}

    def test_filters_out_forbidden_header_names_case_insensitive(self):
        input_data = {
            "Host": "example.com",
            "authorization": "token",
            "CoOkIe": "id=123",
            ":METHOD": "DELETE",
            "Good": "yes",
        }
        assert parse_custom_headers(input_data) == {"Good": "yes"}

    def test_drops_headers_whose_values_contain_CRLF(self):
        input_data = {
            "X-Bad": "evil\r\ninject",
            "X-Good": "safe",
        }
        assert parse_custom_headers(input_data) == {"X-Good": "safe"}

    def test_drops_entire_header_when_array_value_has_any_bad_entry(self):
        input_data = {
            "X-Mixed": ["clean", "bad\nentry"],
            "X-Also-Good": ["ok1", "ok2"],
        }
        assert parse_custom_headers(input_data) == {"X-Also-Good": ["ok1", "ok2"]}

    def test_allows_array_values_when_all_entries_are_clean(self):
        input_data = {"X-Array": ["one", "two", "three"]}
        assert parse_custom_headers(input_data) == {"X-Array": ["one", "two", "three"]}


class TestWsApiPayload(unittest.TestCase):
    def setUp(self):
        self.dummy_config = SimpleNamespace(api_key="test-api-key", api_secret="test-api-secret")
        self.base_payload = {
            "id": "123",
            "params": {
                "some_param": "value",
                "list_param": [1, 2, 3],
                "dict_param": {"nested": "data"}
            }
        }

    def test_payload_with_api_key_and_signed(self):
        websocket_options = WebsocketApiOptions(api_key=True, skip_auth=False, is_signed=True, signer=None)
        
        with patch("binance_common.utils.websocket_api_signature", return_value={"signed": True}) as mock_signature:
            result = ws_api_payload(self.dummy_config, self.base_payload, websocket_options)
            mock_signature.assert_called_once()

            assert result["id"] == self.base_payload["id"]
            assert result["params"] == {"signed": True}

    def test_payload_without_api_key(self):
        websocket_options = WebsocketApiOptions(api_key=False, skip_auth=False, is_signed=False, signer=None)
        result = ws_api_payload(self.dummy_config, self.base_payload, websocket_options)

        assert "apiKey" not in result["params"]
        assert result["id"] == self.base_payload["id"]
        assert isinstance(result["params"]["listParam"], str)
        assert isinstance(result["params"]["dictParam"], str)
        assert result["params"]["someParam"] == "value"

    def test_payload_generates_new_id_if_missing(self):
        websocket_options = WebsocketApiOptions(api_key=True, skip_auth=False, is_signed=False, signer=None)
        payload_without_id = {"params": {}}

        with patch("binance_common.utils.get_uuid", return_value="generated-id"):
            result = ws_api_payload(self.dummy_config, payload_without_id, websocket_options)

            assert result["id"] == "generated-id"

    def test_payload_skips_auth_when_flagged(self):
        websocket_options = WebsocketApiOptions(api_key=True, skip_auth=True, is_signed=False, signer=None)
        result = ws_api_payload(self.dummy_config, self.base_payload, websocket_options)

        assert "apiKey" not in result["params"]

    def test_params_serialization(self):
        websocket_options = WebsocketApiOptions(api_key=False, skip_auth=False, is_signed=False, signer=None)

        result = ws_api_payload(self.dummy_config, self.base_payload, websocket_options)

        assert result["params"]["listParam"] == json.dumps([1, 2, 3], separators=(",", ":"))
        assert result["params"]["dictParam"] == json.dumps({"nested": "data"}, separators=(",", ":"))



class TestWebsocketApiSignature(unittest.TestCase):
    def test_websocket_api_signature(self):
        dummy_config = SimpleNamespace(api_key="test-api-key", api_secret="test-api-secret")
        payload = {"foo": "bar"}

        with patch("binance_common.utils.get_timestamp", return_value=1234567890), \
            patch("binance_common.utils.get_signature", return_value="mocked-signature") as mock_get_signature:

            result = websocket_api_signature(dummy_config, payload)

            assert isinstance(result, OrderedDict)
            assert result["apiKey"] == "test-api-key"
            assert result["timestamp"] == 1234567890
            assert result["foo"] == "bar"
            assert result["signature"] == "mocked-signature"

            mock_get_signature.assert_called_once()
            called_config, called_params, called_signer = mock_get_signature.call_args[0]
            assert called_config == dummy_config
            assert "apiKey=test-api-key" in called_params
            assert "timestamp=1234567890" in called_params


class EventA(BaseModel):
    x: int
    y: str

class EventB(BaseModel):
    a: float
    b: Optional[str]

class UserResponse(BaseModel):
    one_of_schemas: list[str] = ["EventA", "EventB"]
    oneof_schema_eventa_validator: Optional[EventA] = None
    oneof_schema_eventb_validator: Optional[EventB] = None
    actual_instance: Union[EventA, EventB, dict]


class TestGetValidatorFieldMap(unittest.TestCase):

    def test_field_map(self):
        field_map = get_validator_field_map(UserResponse)
        self.assertIn(EventA, field_map)
        self.assertIn(EventB, field_map)
        self.assertEqual(field_map[EventA], "oneof_schema_eventa_validator")
        self.assertEqual(field_map[EventB], "oneof_schema_eventb_validator")


class TestResolveModelFromEvent(unittest.TestCase):

    def test_valid_event(self):
        model_cls = resolve_model_from_event(UserResponse, "eventA")
        self.assertIs(model_cls, EventA)

    def test_invalid_event(self):
        model_cls = resolve_model_from_event(UserResponse, "nonexistent")
        self.assertIsNone(model_cls)

    def test_empty_event(self):
        model_cls = resolve_model_from_event(UserResponse, "")
        self.assertIsNone(model_cls)


class TestParseUserEvent(unittest.TestCase):

    def test_invalid_event(self):
        payload = {"e": "unknown", "data": 123}
        instance = parse_user_event(payload, UserResponse)
        self.assertIsInstance(instance, UserResponse)
        self.assertEqual(instance.actual_instance["data"], 123)

    def test_invalid_payload(self):
        payload = {"e": "eventA", "x": "wrong_type", "y": "hello"}
        instance = parse_user_event(payload, UserResponse)
        self.assertIsInstance(instance, UserResponse)
        self.assertEqual(instance.actual_instance["x"], "wrong_type")

if __name__ == "__main__":
    unittest.main()
