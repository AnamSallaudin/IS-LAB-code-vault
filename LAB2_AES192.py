from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_192_encrypt(plaintext, key):
    # Convert the key and plaintext to bytes
    key_bytes = bytes.fromhex(key)
    plaintext_bytes = plaintext.encode('utf-8')
    
    # Pad plaintext to be a multiple of 16 bytes
    padded_plaintext = pad(plaintext_bytes, AES.block_size)
    
    # Create an AES cipher object using AES-192
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Return the IV and ciphertext for decryption
    return cipher.iv, ciphertext

def aes_192_decrypt(iv, ciphertext, key):
    # Convert the key to bytes
    key_bytes = bytes.fromhex(key)
    
    # Create an AES cipher object for decryption
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    return unpad(decrypted_padded_text, AES.block_size).decode('utf-8')

# Key and message
key = "FEDCBA9876543210FEDCBA9876543210"  # AES-192 key must be 24 bytes
plaintext = "Top Secret Data"

# Encrypt the message
iv, ciphertext = aes_192_encrypt(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message
decrypted_message = aes_192_decrypt(iv, ciphertext, key)
print("Decrypted message:", decrypted_message)
