import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from ..utils.file_operations import read_file, write_file, get_encrypted_file_path


def encrypt_aes(file_path, directory):
    key = get_random_bytes(32)  # 256-bit key
    cipher = AES.new(key, AES.MODE_EAX)
    file_data = read_file(file_path)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    encrypted_file_path = get_encrypted_file_path(file_path)
    encrypted_file_full_path = os.path.join(
        directory, os.path.basename(encrypted_file_path)
    )
    with open(encrypted_file_full_path, "wb") as encrypted_file:
        [encrypted_file.write(x) for x in (cipher.nonce, tag, ciphertext)]
    return key.hex(), encrypted_file_full_path