from functools import lru_cache
import pandas as pd
import uuid as uuid
from db import supabase
from src.securedatatransfer.encryption.asymmetric import layered_rsa_encrypt


def get_mac_address():
    """
    Get the MAC address of the device
    """
    mac = ":".join(
        [
            "{:02x}".format((uuid.getnode() >> elements) & 0xFF)
            for elements in range(0, 2 * 6, 2)
        ][::-1]
    )
    return mac


def insert_file(
    file_name, original_file_name, encryption_method, file_path, key, file_size
):
    """
    Add a new encrypted file details to the database
    """
    data = {
        "file_name": file_name,
        "original_file_name": original_file_name,
        "encryption_method": encryption_method,
        "file_path": file_path,
        "user_id": get_mac_address(),
        "key": encrypt_key(key),
        "file_size": file_size,
    }
    supabase.table("files").insert(data).execute()


def encrypt_key(aes_key):
    """
    Encrypts the AES key with multiple RSA keys and adds the encrypted file details to the database.
    """
    public_key_paths = [
        "assets/keys/public/key01.pem"
        # "assets/keys/public/key02.pem",
        # "assets/keys/public/key03.pem",
    ]
    return layered_rsa_encrypt(aes_key, public_key_paths)

@lru_cache
def read_all_files() -> pd.DataFrame:
    res = supabase.table("files").select("*").execute()
    return pd.DataFrame(res.data)


def delete_file(file_name: str, file_size: int):
    response = (
        supabase.table("files")
        .delete()
        .match({"file_name": file_name, "file_size": file_size})
        .execute()
    )
    return {"data": response.data}