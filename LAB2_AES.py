from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_aes(plaintext, key):
    # Convert the key to bytes and create a new AES cipher object
    key_bytes = key.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of 16 bytes
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    
    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)
    
    # Return the IV and ciphertext for decryption
    return cipher.iv, ciphertext

def decrypt_aes(iv, ciphertext, key):
    # Convert the key to bytes and create a new AES cipher object for decryption
    key_bytes = key.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    return unpad(decrypted_padded_text, AES.block_size).decode('utf-8')

# Key and message
key = "0123456789ABCDEF0123456789ABCDEF"  # AES-128 key must be 16 bytes
plaintext = "Sensitive Information"

# Encrypt the message
iv, ciphertext = encrypt_aes(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message
decrypted_message = decrypt_aes(iv, ciphertext, key)
print("Decrypted message:", decrypted_message)
