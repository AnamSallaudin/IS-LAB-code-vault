from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_aes(plaintext, key):
    # Ensure the key is valid for AES-256 (32 bytes)
    key_bytes = key.encode('utf-8')  # Use the entire key as bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of 16 bytes
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    
    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)
    
    # Return the IV and ciphertext for decryption
    return cipher.iv, ciphertext

def decrypt_aes(iv, ciphertext, key):
    # Convert the key to bytes
    key_bytes = key.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    return unpad(decrypted_padded_text, AES.block_size).decode('utf-8')

# Key and message
key = "0123456789ABCDEF0123456789ABCDEF"  # AES-256 key must be 32 bytes
plaintext = "Encryption Strength"

# Encrypt the message
iv, ciphertext = encrypt_aes(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message
decrypted_message = decrypt_aes(iv, ciphertext, key)
print("Decrypted message:", decrypted_message)
