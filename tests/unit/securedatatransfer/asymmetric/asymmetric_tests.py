import pytest
import os
from src.securedatatransfer.encryption.asymmetric import encrypt_rsa, layered_rsa_encrypt
from src.securedatatransfer.decryption.asymmetric import decrypt_rsa, layered_rsa_decrypt

# Assuming 'assets/keys/public' and 'assets/keys/private' directories contain 'key01.pem' and its pair.
PUBLIC_KEY_PATH = "assets/keys/public/key01.pem"
PRIVATE_KEY_PATH = "assets/keys/private/key01.pem"
TEST_FILE_CONTENT = b"Test message for encryption"
TEST_DIRECTORY = "tmp_test_dir"

@pytest.fixture
def setup_environment(tmp_path):
    # Create temporary directory for test files
    test_dir = tmp_path / TEST_DIRECTORY
    test_dir.mkdir()
    # Path for the temporary test file
    test_file_path = test_dir / "test_file.txt"
    with open(test_file_path, "wb") as f:
        f.write(TEST_FILE_CONTENT)
    return test_dir, test_file_path

def test_encrypt_decrypt_rsa(setup_environment):
    test_dir, test_file_path = setup_environment
    encrypted_file_path = encrypt_rsa(str(test_file_path), PUBLIC_KEY_PATH, str(test_dir))
    assert os.path.exists(encrypted_file_path), "Encryption failed, file not found"

    decrypted_file_path = decrypt_rsa(encrypted_file_path, PRIVATE_KEY_PATH, str(test_dir))
    assert os.path.exists(decrypted_file_path), "Decryption failed, file not found"

    with open(decrypted_file_path, "rb") as f:
        decrypted_content = f.read()
    assert decrypted_content == TEST_FILE_CONTENT, "Decrypted content does not match original"

def test_layered_rsa_encrypt_decrypt():
    # Prepare a test AES key (hex)
    test_aes_key_hex = "a1b2c3d4e5f601234567890abcdef1234567890abcdef1234567890abcdef12"
    # Public keys for layered encryption - using one for simplicity, but could be expanded
    public_key_paths = [PUBLIC_KEY_PATH]
    # Encrypt the AES key
    encrypted_aes_key_hex = layered_rsa_encrypt(test_aes_key_hex, public_key_paths)
    # Decrypt the AES key
    decrypted_aes_key_hex = layered_rsa_decrypt(encrypted_aes_key_hex, PRIVATE_KEY_PATH)
    assert decrypted_aes_key_hex == test_aes_key_hex, "Layered RSA decryption failed to recover original AES key"