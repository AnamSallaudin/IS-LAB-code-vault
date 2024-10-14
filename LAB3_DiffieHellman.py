from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate DH parameters
def generate_dh_parameters():
    return dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Generate DH keys
def generate_dh_keys(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Derive shared secret
def derive_shared_secret(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

# Function to encrypt message using AES
def encrypt_message(message, key):
    salt = os.urandom(16)  # Generate a random salt
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key_bytes = kdf.derive(key)  # Derive AES key from shared secret
    iv = os.urandom(16)  # Generate IV
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return salt + iv + ciphertext  # Return salt, IV, and ciphertext

# Function to decrypt message using AES
def decrypt_message(ciphertext):
    salt = ciphertext[:16]  # Extract salt
    iv = ciphertext[16:32]  # Extract IV
    ciphertext = ciphertext[32:]  # Extract actual ciphertext

    # Use the shared key again to derive the AES key (assuming shared key is available)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key_bytes = kdf.derive(shared_secret)  # Derive AES key from shared secret
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted.decode()

# Generate DH parameters
parameters = generate_dh_parameters()

# Alice's keys
alice_private_key, alice_public_key = generate_dh_keys(parameters)
print("Alice's Public Key:", alice_public_key)

# Bob's keys
bob_private_key, bob_public_key = generate_dh_keys(parameters)
print("Bob's Public Key:", bob_public_key)

# Derive shared secrets
alice_shared_secret = derive_shared_secret(alice_private_key, bob_public_key)
bob_shared_secret = derive_shared_secret(bob_private_key, alice_public_key)

# Verify both shared secrets are the same
assert alice_shared_secret == bob_shared_secret
shared_secret = alice_shared_secret
print("Shared Secret:", shared_secret.hex())

# Message to encrypt
message = "Information"

# Encrypt the message using the shared secret
ciphertext = encrypt_message(message, shared_secret)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message using the shared secret
decrypted_message = decrypt_message(ciphertext)
print("Decrypted Message:", decrypted_message)
