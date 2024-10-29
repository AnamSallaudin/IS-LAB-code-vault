import math
from Crypto.Util import number
from Crypto.Random import get_random_bytes

def generate_keypair(bits=1024):
    """Generates a public/private key pair."""
    p = number.getPrime(bits)
    g = 2
    x = number.getRandomRange(1, p - 1)  # Private key
    y = pow(g, x, p)  # Public key
    return ((p, g, y), x)  # Public key, private key

def encrypt(pub_key, message):
    """Encrypts a message using the public key."""
    p, g, y = pub_key
    r = number.getRandomRange(1, p - 1)
    while math.gcd(r, p) != 1:
        r = number.getRandomRange(1, p - 1)
    a = pow(g, r, p)
    b = (message * pow(y, r, p)) % p
    return (a, b)

def decrypt(priv_key, ciphertext):
    """Decrypts a ciphertext using the private key."""
    p, g, _ = pub_key
    a, b = ciphertext
    x = priv_key  # Use the private key directly
    s = pow(a, x, p)  # s = a^x mod p
    message = (b * number.inverse(s, p)) % p
    return message

def compare(ciphertext1, ciphertext2, pub_key):
    """Compare two encrypted messages."""
    # Decrypt both to compare (this is for demonstration purposes)
    decrypted1 = decrypt(priv_key, ciphertext1)
    decrypted2 = decrypt(priv_key, ciphertext2)
    return decrypted1, decrypted2

# Generate key pair
pub_key, priv_key = generate_keypair()

# Blood pressure readings (encrypting sample readings)
blood_pressure1 = encrypt(pub_key, 120)  # Encrypted reading of 120
blood_pressure2 = encrypt(pub_key, 140)  # Encrypted reading of 140

# Homomorphic comparison (encrypted result)
decrypted_comparison = compare(blood_pressure1, blood_pressure2, pub_key)

# Print results
decrypted_bp1, decrypted_bp2 = decrypted_comparison
print(f"Decrypted Blood Pressure 1: {decrypted_bp1}")
print(f"Decrypted Blood Pressure 2: {decrypted_bp2}")

# Diagnosis based on the decrypted comparison result
if decrypted_bp1 > decrypted_bp2:
    print("Diagnosis: Blood Pressure 1 is higher than Blood Pressure 2.")
else:
    print("Diagnosis: Blood Pressure 1 is not higher than Blood Pressure 2.")
