import pytest, os
from Crypto.Random import get_random_bytes
from src.securedatatransfer.encryption.symmetric import encrypt_aes
from src.securedatatransfer.decryption.symmetric import decrypt_aes
from src.securedatatransfer.utils.file_operations import write_file, read_file


@pytest.fixture
def setup_files(tmp_path):
    """Create a sample file for testing."""
    original_file = tmp_path / "original.txt"
    original_file.write_text("This is some test data for AES encryption.")
    return str(original_file)


def test_encrypt_aes(setup_files, tmp_path):
    original_file = setup_files
    directory = str(tmp_path)

    # Encrypt the file
    key, encrypted_file_path = encrypt_aes(original_file, directory)

    # Check that the encrypted file exists and the name is correct
    assert os.path.exists(encrypted_file_path), "Encrypted file should be created"
    assert encrypted_file_path.endswith(
        ".enc"
    ), "The encrypted file should have an '.enc' extension"