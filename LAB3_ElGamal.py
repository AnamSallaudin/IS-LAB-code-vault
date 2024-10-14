import random
from sympy import mod_inverse

# Function to generate a random prime
def generate_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# Simple primality test
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate ElGamal keys
def generate_keys():
    p = generate_prime(16)  # Generate a prime p
    g = random.randint(2, p-1)  # Choose a generator g
    x = random.randint(1, p-2)  # Private key x
    h = pow(g, x, p)  # Public key h
    return (p, g, h), x  # Return public key and private key

# Encrypt the message
def encrypt(public_key, message):
    p, g, h = public_key
    m = int.from_bytes(message.encode(), 'big')  # Convert message to an integer
    y = random.randint(1, p-2)  # Random y
    c1 = pow(g, y, p)  # c1 = g^y mod p
    s = pow(h, y, p)  # s = h^y mod p
    c2 = (m * s) % p  # c2 = (m * s) mod p
    return c1, c2  # Return ciphertext (c1, c2)

# Decrypt the message
def decrypt(private_key, public_key, ciphertext):
    p, _, _ = public_key
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)  # s = c1^x mod p
    s_inv = mod_inverse(s, p)  # Compute s^{-1}
    m = (c2 * s_inv) % p  # m = (c2 * s^{-1}) mod p
    # Convert integer back to bytes
    message_length = (m.bit_length() + 7) // 8
    return m.to_bytes(message_length, 'big').decode()  # Return decrypted message

# Main execution
public_key, private_key = generate_keys()
message = "Confidential Data"

# Encrypt the message
ciphertext = encrypt(public_key, message)
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt(private_key, public_key, ciphertext)
print(f"Decrypted Message: {decrypted_message}")
