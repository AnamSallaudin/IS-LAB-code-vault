from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

def encrypt_3des(plaintext, key):
    # Ensure the key is valid for 3DES (24 bytes)
    key_bytes = key.encode('utf-8')[:24]  # Use the first 24 bytes
    cipher = DES3.new(key_bytes, DES3.MODE_CBC)
    
    # Pad the plaintext to be a multiple of 8 bytes
    padded_text = pad(plaintext.encode('utf-8'), DES3.block_size)
    
    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)
    
    # Return the IV and ciphertext for decryption
    return cipher.iv, ciphertext

def decrypt_3des(iv, ciphertext, key):
    # Ensure the key is valid for 3DES (24 bytes)
    key_bytes = key.encode('utf-8')[:24]  # Use the first 24 bytes
    cipher = DES3.new(key_bytes, DES3.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    return unpad(decrypted_padded_text, DES3.block_size).decode('utf-8')

# Key and message
key = "1234567890ABCDEF1234567890ABCDEF"  # Use first 24 bytes for 3DES
plaintext = "Classified Text"

# Encrypt the message
iv, ciphertext = encrypt_3des(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message
decrypted_message = decrypt_3des(iv, ciphertext, key)
print("Decrypted message:", decrypted_message)
