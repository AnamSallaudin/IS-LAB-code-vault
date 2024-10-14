import random
from sympy import isprime, mod_inverse

class RSA:
    def __init__(self, bit_length=512):
        self.p, self.q = self._generate_large_primes(bit_length)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self._choose_e(self.phi)
        self.d = mod_inverse(self.e, self.phi)

    def _generate_large_primes(self, bit_length):
        p = self._generate_large_prime(bit_length)
        q = self._generate_large_prime(bit_length)
        return p, q

    def _generate_large_prime(self, bit_length):
        while True:
            num = random.getrandbits(bit_length)
            if isprime(num):
                return num

    def _choose_e(self, phi):
        e = 65537  # Commonly used prime exponent
        if e < phi and gcd(e, phi) == 1:
            return e
        raise ValueError("Unable to find a valid e")

    def encrypt(self, plaintext):
        if plaintext < 0 or plaintext >= self.n:
            raise ValueError("Plaintext must be in range [0, n).")
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

    def multiply_encrypted(self, c1, c2):
        return (c1 * c2) % self.n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    # Initialize RSA
    rsa = RSA()

    # Encrypt two integers
    m1 = 7
    m2 = 3
    c1 = rsa.encrypt(m1)
    c2 = rsa.encrypt(m2)

    print(f"Ciphertext of {m1}: {c1}")
    print(f"Ciphertext of {m2}: {c2}")

    # Perform multiplication on encrypted integers
    c_product = rsa.multiply_encrypted(c1, c2)
    print(f"Ciphertext of product: {c_product}")

    # Decrypt the result
    decrypted_product = rsa.decrypt(c_product)
    print(f"Decrypted product: {decrypted_product}")

    # Verify the result
    print(f"Original product: {m1 * m2}")
