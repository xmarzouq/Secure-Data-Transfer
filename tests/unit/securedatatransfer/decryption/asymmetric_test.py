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


def test_decrypt_rsa(rsa_keys, test_files, tmp_path):
    _, priv_key_path = rsa_keys
    original_file = test_files

    encrypted_file_path = encrypt_rsa(str(original_file), rsa_keys[0], str(tmp_path))
    decrypted_file_path = decrypt_rsa(encrypted_file_path, priv_key_path, str(tmp_path))
    decrypted_file = tmp_path / decrypted_file_path

    assert decrypted_file.exists(), "Decrypted file should be created"
    assert (
        decrypted_file.read_text() == original_file.read_text()
    ), "Decrypted content must match the original"
    assert (
        decrypted_file.name == original_file.name
    ), "Decrypted file name should match the original without '.enc'"


def test_layered_encryption(rsa_keys):
    """Test layered RSA encryption and decryption of an AES key."""
    pub_key_path, priv_key_path = rsa_keys
    original_aes_key = get_random_bytes(32)
    original_aes_key_hex = original_aes_key.hex()

    encrypted_aes_key_hex = layered_rsa_encrypt(original_aes_key_hex, [pub_key_path])

    decrypted_aes_key_hex = layered_rsa_decrypt(encrypted_aes_key_hex, priv_key_path)

    assert (
        original_aes_key_hex == decrypted_aes_key_hex
    ), "Decrypted AES key must match the original"