from sympy import mod_inverse
import random

# Parameters
p = 7919
g = 2
h = 6465
x = 2999

# Function to encrypt a message
def encrypt(message):
    # Convert message to an integer (simple encoding)
    m = int.from_bytes(message.encode('utf-8'), 'big')

    # Choose a random integer y
    y = random.randint(1, p - 2)  # y should be in the range (1, p-1)

    # Calculate c1 and s
    c1 = pow(g, y, p)
    s = pow(h, y, p)

    # Calculate c2
    c2 = (m * s) % p

    return (c1, c2)

# Function to decrypt the ciphertext
def decrypt(ciphertext):
    c1, c2 = ciphertext

    # Calculate s = c1^x mod p
    s = pow(c1, x, p)

    # Calculate s inverse
    s_inv = mod_inverse(s, p)

    # Retrieve the original message
    m = (c2 * s_inv) % p

    # Convert integer back to bytes and decode
    byte_length = (m.bit_length() + 7) // 8
    message_bytes = m.to_bytes(byte_length, 'big')
    return message_bytes.decode('utf-8', errors='ignore')  # Use 'ignore' to handle decoding issues

# Message to encrypt
message = "Asymmetric Algorithms"

# Encrypt the message
ciphertext = encrypt(message)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_message = decrypt(ciphertext)
print("Decrypted Message:", decrypted_message)
