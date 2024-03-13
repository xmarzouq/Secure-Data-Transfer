from Crypto.PublicKey import RSA
import os

# Specify the directory where you want to save the keys
key_dir = 'assets/keys/'

# Create the "keys" directory if it doesn't exist
if not os.path.exists(key_dir):
    os.makedirs(key_dir)

# Generate an RSA key pair with a specified key size (e.g., 2048 bits)
key = RSA.generate(2048)

# Extract the public and private keys
public_key = key.publickey().export_key()
private_key = key.export_key()

# Specify the file paths for the keys
public_key_path = os.path.join(key_dir, 'public_key.pem')
private_key_path = os.path.join(key_dir, 'private_key.pem')

# Save the keys to the specified directory
with open(public_key_path, 'wb') as public_key_file:
    public_key_file.write(public_key)

with open(private_key_path, 'wb') as private_key_file:
    private_key_file.write(private_key)

# Print the paths to the saved keys (optional)
print(f"Public key saved to: {public_key_path}")
print(f"Private key saved to: {private_key_path}")