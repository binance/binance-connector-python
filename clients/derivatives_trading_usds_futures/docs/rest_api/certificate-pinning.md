# Certificate Pinning

```python
import ssl
import base64
import hashlib

from socket import create_connection
from OpenSSL.crypto import dump_publickey, load_certificate, FILETYPE_ASN1

from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import DerivativesTradingUsdsFutures
from binance_sdk_derivatives_trading_usds_futures.rest_api.models import ExchangeInformationResponse

PINNED_PUBLIC_KEY = "YOUR-PINNED-PUBLIC-KEY"
CA_CERT_PATH = "/path/to/certificate.pem"

def verify_certificate(hostname, port=443):
    """Retrieve the certificate, extract the public key, and verify its hash."""
    # Establish an SSL connection
    context = ssl.create_default_context()
    conn = context.wrap_socket(create_connection((hostname, port)), server_hostname=hostname)
    
    # Get the certificate in DER format
    der_cert = conn.getpeercert(binary_form=True)
    conn.close()

    # Convert DER to X.509 certificate
    x509 = load_certificate(FILETYPE_ASN1, der_cert)

    # Extract public key
    pubkey_der = dump_publickey(FILETYPE_ASN1, x509.get_pubkey())

    # Compute the SHA-256 hash of the public key
    public_key_hash = base64.b64encode(hashlib.sha256(pubkey_der).digest()).decode()

    # Validate public key hash against the pinned key
    if public_key_hash != PINNED_PUBLIC_KEY:
        raise ssl.SSLError(f"Certificate pinning validation failed: expected {PINNED_PUBLIC_KEY}, got {public_key_hash}")

class PinnedSSLContext(ssl.SSLContext):
    def __init__(self, hostname):
        super().__init__(ssl.PROTOCOL_TLS_CLIENT)
        self.verify_mode = ssl.CERT_REQUIRED
        self.load_verify_locations(CA_CERT_PATH)
        verify_certificate(hostname)

ssl_context = PinnedSSLContext("fapi.binance.com")

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl_context,
)
client = DerivativesTradingUsdsFutures(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_information()
    data: ExchangeInformationResponse = response.data()
    print(data)
except ssl.SSLError as ssl_err:
    print("SSL Certificate validation failed! Possible MITM attack.", ssl_err)
except Exception as err:
    print("An error occurred:", err)
```
