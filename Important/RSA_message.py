from Crypto.Util import number
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA keys
def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt the message using RSA
def encrypt_message(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

# Main function
if __name__ == "__main__":
    private_key, public_key = generate_keypair()
    
    message = "Hello"
    encrypted_message = encrypt_message(public_key, message)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
