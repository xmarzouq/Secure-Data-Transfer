from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from ..utils.file_operations import read_file, write_file, get_encrypted_file_path
import os

MAX_RSA_BLOCK_SIZE = 214


def encrypt_rsa(file_path, public_key_path, directory):
    try:
        recipient_public_key = RSA.import_key(read_file(public_key_path))
        file_data = read_file(file_path)
        cipher_rsa = PKCS1_OAEP.new(recipient_public_key)

        encrypted_data = b""
        for i in range(0, len(file_data), MAX_RSA_BLOCK_SIZE):
            block = file_data[i : i + MAX_RSA_BLOCK_SIZE]
            encrypted_block = cipher_rsa.encrypt(block)
            encrypted_data += encrypted_block

        encrypted_file_path = get_encrypted_file_path(file_path)
        encrypted_file_full_path = os.path.join(
            directory, os.path.basename(encrypted_file_path)
        )
        write_file(encrypted_file_full_path, encrypted_data)
        return encrypted_file_full_path
    except Exception as e:
        return False, str(e)