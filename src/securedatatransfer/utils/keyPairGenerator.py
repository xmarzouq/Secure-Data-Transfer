from Crypto.PublicKey import RSA
import os

key_dir = 'assets/keys/'
if not os.path.exists(key_dir):
    os.makedirs(key_dir)
key = RSA.generate(2048)


public_key = key.publickey().export_key()
private_key = key.export_key()

public_key_path = os.path.join(key_dir, 'public_key.pem')
private_key_path = os.path.join(key_dir, 'private_key.pem')

with open(public_key_path, 'wb') as public_key_file:
    public_key_file.write(public_key)
with open(private_key_path, 'wb') as private_key_file:
    private_key_file.write(private_key)

print(f"Public key saved to: {public_key_path}")
print(f"Private key saved to: {private_key_path}")