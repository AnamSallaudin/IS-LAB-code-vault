from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Print keys for reference
print("Public Key:")
print(public_key.decode())
print("\nPrivate Key:")
print(private_key.decode())

# Encrypt the message using the public key
def encrypt_message(message, pub_key):
    rsa_pub_key = RSA.import_key(pub_key)
    cipher = PKCS1_OAEP.new(rsa_pub_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted)

# Decrypt the message using the private key
def decrypt_message(encrypted_message, priv_key):
    rsa_priv_key = RSA.import_key(priv_key)
    cipher = PKCS1_OAEP.new(rsa_priv_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode()

# Message to encrypt
message = "Asymmetric Encryption"

# Encrypt the message
encrypted_message = encrypt_message(message, public_key)
print("\nEncrypted Message (Base64):")
print(encrypted_message.decode())

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, private_key)
print("\nDecrypted Message:")
print(decrypted_message)
