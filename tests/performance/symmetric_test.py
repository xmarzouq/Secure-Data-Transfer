import pytest
import time
from src.securedatatransfer.encryption.symmetric import encrypt_aes
from src.securedatatransfer.decryption.symmetric import decrypt_aes


@pytest.fixture
def test_files():
    small_file_path = "assets/temp/small_file.pdf"
    large_file_path = "assets/temp/large_file.txt"
    return small_file_path, large_file_path


def test_aes_performance(test_files, tmp_path):
    small_file, large_file = test_files
    encryption_times = {"small": [], "large": []}
    decryption_times = {"small": [], "large": []}

    for file in [small_file, large_file]:
        file_size = "small" if file == small_file else "large"
        for _ in range(100):
            start_time = time.time()
            key, encrypted_file_path = encrypt_aes(str(file), str(tmp_path))
            encryption_times[file_size].append(time.time() - start_time)
            start_time = time.time()
            decrypt_aes(encrypted_file_path, key, str(tmp_path))
            decryption_times[file_size].append(time.time() - start_time)
        avg_encryption_time = sum(encryption_times[file_size]) / len(
            encryption_times[file_size]
        )
        avg_decryption_time = sum(decryption_times[file_size]) / len(
            decryption_times[file_size]
        )
        print(
            "\n============================================================================================================================================="
        )
        print(
            f"\n\t\t\t\t\t\tAverage encryption time for {file_size} file (~10 MB): {avg_encryption_time:.3f}s"
        )
        print(
            f"\t\t\t\t\t\tAverage decryption time for {file_size} file (~100 MB): {avg_decryption_time:.3f}s"
        )
    print(
        "\n============================================================================================================================================="
    )
    print(
        f"\t\t\t\t\tTOTAL FILES ENCRYPTED AND DECRYPTED \nUSING SYMMETRIC ENCRYPTION: 200\n"
    )
    assert avg_encryption_time <= 5
    assert avg_decryption_time <= 20