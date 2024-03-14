from Crypto.Cipher import AES
from ..utils.file_operations import read_file, write_file, get_decrypted_file_path
import os


def decrypt_aes(encrypted_file_path, key, directory):
    data = read_file(encrypted_file_path)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(bytes.fromhex(key), AES.MODE_EAX, nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    decrypted_file_path = get_decrypted_file_path(encrypted_file_path)
    decrypted_file_full_path = os.path.join(
        directory, os.path.basename(decrypted_file_path)
    )
    write_file(decrypted_file_full_path, decrypted_data)
    return decrypted_file_full_path