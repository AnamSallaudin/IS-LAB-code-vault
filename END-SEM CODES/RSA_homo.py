import random
from Crypto.Util import number

def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Return the modular inverse of a modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair(bits=1024):
    """Generates a public/private key pair."""
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Common choice for e
    d = modinv(e, phi)
    
    return ((n, e), (n, d))  # Public key, private key

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    n, e = public_key
    # Convert plaintext to bytes and then to an integer
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_int = int.from_bytes(plaintext_bytes, byteorder='big')
    
    # Encrypt the plaintext integer
    ciphertext_int = pow(plaintext_int, e, n)
    return ciphertext_int

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    n, d = private_key
    # Decrypt the ciphertext integer
    decrypted_int = pow(ciphertext, d, n)
    # Convert the decrypted integer back to bytes
    byte_length = (decrypted_int.bit_length() + 7) // 8
    decrypted_bytes = decrypted_int.to_bytes(byte_length, byteorder='big')
    return decrypted_bytes.decode('utf-8', errors='ignore')  # Decode to string

def read_file(filename):
    """Read the contents of a file."""
    with open(filename, 'r') as file:
        return file.read()

def main():
    # Generate RSA key pair
    public_key, private_key = generate_keypair(512)  # 512 bits for quicker demonstration
    
    # Encrypt messages from two text files
    for filename in ['message1.txt', 'message2.txt']:
        try:
            message = read_file(filename)
            ciphertext = encrypt(public_key, message)
            print(f"Ciphertext for {filename}: {ciphertext}")

            # Decrypt the ciphertext
            decrypted_message = decrypt(private_key, ciphertext)
            print(f"Decrypted message for {filename}: {decrypted_message}\n")
        except FileNotFoundError:
            print(f"File not found: {filename}")

if __name__ == "__main__":
    main()
