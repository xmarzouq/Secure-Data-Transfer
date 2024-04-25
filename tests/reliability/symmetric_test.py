import pytest
import os
from src.securedatatransfer.encryption.symmetric import encrypt_aes
from src.securedatatransfer.decryption.symmetric import decrypt_aes
from src.securedatatransfer.utils.file_operations import read_file, write_file


@pytest.fixture
def test_file(tmp_path):
    small_file_path = "assets/temp/small_file.pdf"
    return str(small_file_path)


def test_aes_reliability(test_file):
    file_path = test_file
    success_count = 0
    failure_count = 0
    test_cycles = 500

    for _ in range(test_cycles):
        key, encrypted_file_path = encrypt_aes(file_path, os.path.dirname(file_path))
        decrypted_file_path = decrypt_aes(
            encrypted_file_path, key, os.path.dirname(file_path)
        )
        original_content = read_file(file_path)
        decrypted_content = read_file(decrypted_file_path)
        if original_content == decrypted_content:
            success_count += 1
        else:
            failure_count += 1
    success_rate = (success_count / test_cycles) * 100
    print(
        "\n==============================================================================================================================="
    )
    print(f"\n\t\t\t\t\t\t\tTotal success count: {success_count}")
    print(f"\t\t\t\t\t\t\tTotal failure count: {failure_count}")
    print(f"\t\t\t\t\t\t\tSuccess rate: {success_rate:.3f}%")
    print(
        "\n==============================================================================================================================="
    )
    assert success_rate >= 99.9, "Reliability target of 99.9% success rate not met"