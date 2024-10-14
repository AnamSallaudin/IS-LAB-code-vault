# RSA Parameters
n = 323
e = 5
d = 173

# Function to convert string to integer
def string_to_int(message):
    return int.from_bytes(message.encode('utf-8'), 'big')

# Function to convert integer back to string
def int_to_string(number):
    byte_length = (number.bit_length() + 7) // 8  # Calculate byte length
    return number.to_bytes(byte_length, 'big').decode('utf-8', errors='ignore')

# RSA Encryption
def rsa_encrypt(message):
    plaintext = string_to_int(message)  # Convert message to integer
    ciphertext = pow(plaintext, e, n)   # Encrypt using the formula
    return ciphertext

# RSA Decryption
def rsa_decrypt(ciphertext):
    plaintext = pow(ciphertext, d, n)    # Decrypt using the formula
    return int_to_string(plaintext)      # Convert integer back to string

# Message to encrypt
message = "Cryptographic Protocols"

# Encrypt the message
ciphertext = rsa_encrypt(message)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_message = rsa_decrypt(ciphertext)
print("Decrypted Message:", decrypted_message)
