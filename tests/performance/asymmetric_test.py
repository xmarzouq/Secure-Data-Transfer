import pytest
from Crypto.PublicKey import RSA
from src.securedatatransfer.encryption.asymmetric import encrypt_rsa
from src.securedatatransfer.decryption.asymmetric import decrypt_rsa
import time


@pytest.fixture(scope="module")
def rsa_keys(tmp_path_factory):
    key = RSA.generate(2048)
    pub_key_path = tmp_path_factory.mktemp("keys") / "public_key.pem"
    priv_key_path = tmp_path_factory.mktemp("keys") / "private_key.pem"
    with open(pub_key_path, "wb") as f:
        f.write(key.publickey().export_key())
    with open(priv_key_path, "wb") as f:
        f.write(key.export_key())
    return str(pub_key_path), str(priv_key_path)


@pytest.fixture
def test_files_rsa(tmp_path):
    small_file = tmp_path / "small_file.txt"
    large_file = tmp_path / "large_file.txt"
    small_file.write_text("Small file content" * 87382)
    large_file.write_text("Large file content" * 87382 * 100)
    return str(small_file), str(large_file)


def test_rsa_performance(rsa_keys, test_files_rsa, tmp_path):
    pub_key_path, priv_key_path = rsa_keys
    small_file_path, large_file_path = test_files_rsa
    encryption_times = {"small": [], "large": []}
    decryption_times = {"small": [], "large": []}

    for file_path in [small_file_path, large_file_path]:
        file_size = "small" if "small" in file_path else "large"

        for _ in range(100):
            start_enc = time.time()
            encrypted_file_path = encrypt_rsa(file_path, pub_key_path, str(tmp_path))
            encryption_times[file_size].append(time.time() - start_enc)

            start_dec = time.time()
            decrypt_rsa(encrypted_file_path, priv_key_path, str(tmp_path))
            decryption_times[file_size].append(time.time() - start_dec)

        avg_encryption_time = sum(encryption_times[file_size]) / len(
            encryption_times[file_size]
        )
        avg_decryption_time = sum(decryption_times[file_size]) / len(
            decryption_times[file_size]
        )
        print(
            "\n=================================================================================================================================================================================="
        )
        print(
            f"\n\t\t\t\t\t\tAverage encryption time for {file_size} file (~10 MB): {avg_encryption_time:.3f}s"
        )
        print(
            f"\t\t\t\t\t\tAverage decryption time for {file_size} file (~100 MB): {avg_decryption_time:.3f}s"
        )

    print(
        "\n=================================================================================================================================================================================="
    )
    print(
        f"\t\t\t\t\t\tTOTAL FILES ENCRYPTED  AND DECRYPTED USING ASYMMETRIC ENCRYPTION: 200\n"
    )