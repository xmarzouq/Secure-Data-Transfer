import pytest
import os
from src.securedatatransfer.encryption.asymmetric import encrypt_rsa
from src.securedatatransfer.decryption.asymmetric import decrypt_rsa
from src.securedatatransfer.utils.file_operations import read_file, write_file
from Crypto.PublicKey import RSA

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
def test_file_rsa(tmp_path):
    # small_file_path = tmp_path / "small_file.txt"
    # small_file_path.write_text("Hello, this is a test file content for RSA encryption and decryption reliability testing!" * 100)
    # return str(small_file_path)
    small_file_path = "assets/temp/small_file.pdf"
    return str(small_file_path)

def test_rsa_reliability(rsa_keys, test_file_rsa):
    pub_key_path, priv_key_path = rsa_keys
    file_path = test_file_rsa
    success_count = 0
    failure_count = 0
    test_cycles = 500

    for _ in range(test_cycles):
        encrypted_file_path = encrypt_rsa(file_path, pub_key_path, os.path.dirname(file_path))
        decrypted_file_path = decrypt_rsa(
            encrypted_file_path, priv_key_path, os.path.dirname(file_path)
        )
        original_content = read_file(file_path)
        decrypted_content = read_file(decrypted_file_path)
        if original_content == decrypted_content:
            success_count += 1
        else:
            failure_count += 1
    success_rate = (success_count / test_cycles) * 100
    print(
        "\n============================================================================================================================================="
    )
    print(f"\n\t\t\t\t\t\t\tTotal success count: {success_count}")
    print(f"\t\t\t\t\t\t\tTotal failure count: {failure_count}")
    print(f"\t\t\t\t\t\t\tSuccess rate: {success_rate:.3f}%")
    print(
        "\n============================================================================================================================================="
    )
    assert success_rate >= 99.9, "Reliability target of 99.9% success rate not met"
