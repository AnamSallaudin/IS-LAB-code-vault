from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des(plaintext, key):
    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of 8 bytes
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    
    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)
    
    # Return the IV and ciphertext for decryption
    return cipher.iv, ciphertext

def decrypt_des(iv, ciphertext, key):
    # Create a DES cipher object for decryption
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text
    return unpad(decrypted_padded_text, DES.block_size).decode('utf-8')

# Key and message
key = "A1B2C3D4"
plaintext = "Confidential Data"

# Encrypt the message
iv, ciphertext = encrypt_des(plaintext, key)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt the message
decrypted_message = decrypt_des(iv, ciphertext, key)
print("Decrypted message:", decrypted_message)
