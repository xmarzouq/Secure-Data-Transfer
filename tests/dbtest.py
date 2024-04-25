from repo import insert_file

# Example data to insert
file_data = {
    "file_name": "secure-doc.pdf",
    "original_file_name": "document.pdf",
    "encryption_method": "AES-256",
    "file_path": "/path/to/encrypted/files/secure-doc.pdf",
    "user_id": "user_12345",
    "key": "encryption_key_here",
    "file_size": 1024  # Size in bytes
}

# Insert the file
response = insert_file(file_data)

# Print the response to verify
print(response)