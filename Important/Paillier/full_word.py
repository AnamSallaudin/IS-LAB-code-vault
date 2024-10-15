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

# Decryption
def decrypt(private_key, public_key, ciphertext):
    n, g = public_key
    lambda_n = private_key
    # Calculate the plaintext
    plaintext = (pow(ciphertext, lambda_n, n**2) - 1) // n
    return plaintext

# Main function
if __name__ == "__main__":
    # Generate keypair
    public_key, lambda_n = generate_keypair(bits=32)
    word = 'Today'
    
    # Combine ASCII values into a single integer (simple encoding)
    combined_message = sum(ord(char) * (256 ** i) for i, char in enumerate(reversed(word)))

    # Encrypt the combined message
    encrypted_message = encrypt(public_key, combined_message)

    # Display encrypted message
    print(f"Original Message: '{word}'")
    print(f"Combined ASCII as Integer: {combined_message}")
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the encrypted message
    decrypted_message = decrypt(lambda_n, public_key, encrypted_message)

    # Split the decrypted integer back into characters
    decoded_chars = []
    while decrypted_message > 0:
        decoded_chars.append(chr(decrypted_message % 256))  # Get the last character
        decrypted_message //= 256  # Move to the next character

    # Since we encoded the message in reverse order, reverse to get the original order
    decoded_chars.reverse()
    result_string = ''.join(decoded_chars)

    # Display decrypted message
    print(f"Decrypted Message: '{result_string}'")

    # Ensure that the decryption matches the original string
    if result_string == word:
        print("Decryption successful!")
    else:
        print("Decryption failed!")
