import pytest
from unittest.mock import patch, mock_open
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from src.securedatatransfer.encryption.asymmetric import (
    encrypt_rsa,
    layered_rsa_encrypt,
)
from src.securedatatransfer.decryption.asymmetric import (
    decrypt_rsa,
    layered_rsa_decrypt,
)


@pytest.fixture(scope="module")
def rsa_keys(tmp_path_factory):
    """Generate RSA keys once per test session and simulate their storage."""
    key = RSA.generate(2048)
    pub_key_path = tmp_path_factory.mktemp("keys") / "pub_key.pem"
    priv_key_path = tmp_path_factory.mktemp("keys") / "priv_key.pem"
    pub_key_path.write_bytes(key.publickey().export_key())
    priv_key_path.write_bytes(key.export_key())
    return str(pub_key_path), str(priv_key_path)


@pytest.fixture
def test_files(tmp_path):
    """Create sample files for testing."""
    original_file = tmp_path / "original.txt"
    original_file.write_text("This is some test data.")
    return original_file


def test_encrypt_rsa(rsa_keys, test_files, tmp_path):
    pub_key_path, _ = rsa_keys
    original_file = test_files
    encrypted_file_path = encrypt_rsa(str(original_file), pub_key_path, str(tmp_path))
    assert encrypted_file_path.endswith(
        ".enc"
    ), "The encrypted file should have an '.enc' extension"
    assert tmp_path.joinpath(
        encrypted_file_path
    ).exists(), "Encrypted file should be created"