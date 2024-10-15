import random

# Function to generate a random prime number
def generate_prime(bits=512):
    while True:
        prime = random.getrandbits(bits)
        if is_prime(prime):
            return prime

# Simple primality test
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Key generation for Paillier
def generate_keypair(bits=512):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    g = n + 1  # g is usually n + 1
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
    return (n, g), lambda_n

# GCD function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Encryption
def encrypt(public_key, message):
    n, g = public_key
    r = random.randint(1, n - 1)  # Random r
    c = (pow(g, message, n**2) * pow(r, n, n**2)) % (n**2)  # Ciphertext
    return c

# Main function
if __name__ == "__main__":
    # Generate keypair
    public_key, lambda_n = generate_keypair(bits=32)
    word = 'Today'
    
    # Encrypt each character in the word
    for char in word:
        message = ord(char)  # ASCII value for the character
        
        # Encrypt the message
        encrypted_message = encrypt(public_key, message)

        # Display results
        print(f"Original Character: '{char}' (ASCII: {message})")
        print(f"Encrypted Message: {encrypted_message}")
