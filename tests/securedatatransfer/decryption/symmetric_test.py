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


def test_decrypt_aes(setup_files, tmp_path):
    original_file = setup_files
    directory = str(tmp_path)

    # Encrypt the file first to get the encrypted version and key
    key, encrypted_file_path = encrypt_aes(original_file, directory)

    # Decrypt the encrypted file
    decrypted_file_path = decrypt_aes(encrypted_file_path, key, directory)

    assert os.path.exists(decrypted_file_path), "Decrypted file should be created"
    original_content = read_file(original_file)
    decrypted_content = read_file(decrypted_file_path)
    assert (
        original_content == decrypted_content
    ), "Decrypted content must match the original"