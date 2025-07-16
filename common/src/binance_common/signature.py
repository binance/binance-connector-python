import os

from Crypto.PublicKey import ECC, RSA
from Crypto.Signature import eddsa, pkcs1_15
from typing import Dict, Optional, Tuple, Union


class Signers:
    _rsa_keys: Dict[Tuple[str, Optional[str]], RSA.RsaKey] = {}
    _rsa_signers: Dict[Tuple[str, Optional[str]], pkcs1_15.PKCS115_SigScheme] = {}

    _ed25519_keys: Dict[Tuple[str, Optional[str]], ECC.EccKey] = {}
    _ed25519_signers: Dict[Tuple[str, Optional[str]], object] = {}

    @staticmethod
    def _load_private_key_data(key_input: str) -> str:
        """Load private key content from path or raw string."""
        if os.path.exists(key_input):
            with open(key_input, "r") as f:
                return f.read()
        return key_input

    @classmethod
    def get_rsa_key(cls, key: str, passphrase: Optional[str]) -> RSA.RsaKey:
        key_data = cls._load_private_key_data(key)
        cache_key = (key_data, passphrase)
        if cache_key not in cls._rsa_keys:
            cls._rsa_keys[cache_key] = RSA.import_key(key_data, passphrase=passphrase)
        return cls._rsa_keys[cache_key]

    @classmethod
    def get_rsa_signer(
        cls, key: str, passphrase: Optional[str]
    ) -> pkcs1_15.PKCS115_SigScheme:
        cache_key = (cls._load_private_key_data(key), passphrase)
        if cache_key not in cls._rsa_signers:
            rsa_key = cls.get_rsa_key(key, passphrase)
            cls._rsa_signers[cache_key] = pkcs1_15.new(rsa_key)
        return cls._rsa_signers[cache_key]

    @classmethod
    def get_ed25519_key(cls, key: str, passphrase: Optional[str]) -> ECC.EccKey:
        key_data = cls._load_private_key_data(key)
        cache_key = (key_data, passphrase)
        if cache_key not in cls._ed25519_keys:
            cls._ed25519_keys[cache_key] = ECC.import_key(
                key_data, passphrase=passphrase
            )
        return cls._ed25519_keys[cache_key]

    @classmethod
    def get_ed25519_signer(cls, key: str, passphrase: Optional[str]) -> object:
        cache_key = (cls._load_private_key_data(key), passphrase)
        if cache_key not in cls._ed25519_signers:
            ed_key = cls.get_ed25519_key(key, passphrase)
            cls._ed25519_signers[cache_key] = eddsa.new(ed_key, "rfc8032")
        return cls._ed25519_signers[cache_key]
    
    @classmethod
    def get_signer(cls, private_key: str, passphrase: Optional[str] = None) -> Union[pkcs1_15.PKCS115_SigScheme, object]:
        """
        Automatically detects the key type (RSA or Ed25519) and returns the appropriate signer.
        Raises ValueError if the key is not supported.
        """

        try:
            return cls.get_rsa_signer(private_key, passphrase)
        except (ValueError, IndexError, TypeError):
            pass

        try:
            return cls.get_ed25519_signer(private_key, passphrase)
        except (ValueError, IndexError, TypeError):
            pass

        raise ValueError("Unsupported or invalid private key format. Private key must be either 'RSA' or 'ED25519'")
