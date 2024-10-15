import socket
import random
from sympy import isprime, mod_inverse

# Function to generate prime numbers
def generate_prime(bits=32):
    while True:
        prime = random.getrandbits(bits)
        if isprime(prime):
            return prime

# RSA Key Generation
def generate_keypair():
    p = generate_prime(32)
    q = generate_prime(32)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi_n)  # Compute d
    return (e, n), d  # Return public key and private key

# RSA Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = pow(plaintext, e, n)  # c = m^e mod n
    return cipher

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server is listening for connections...")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # Generate keys
        public_key, private_key = generate_keypair()
        print("Keys generated.")
        
        # Send public key
        conn.sendall(f"{public_key[0]},{public_key[1]}".encode())
        
        # Send private key (for demo purposes only!)
        conn.sendall(str(private_key).encode())
        
        # Encrypt a message
        message = "Hello, Client!"
        message_int = int.from_bytes(message.encode(), 'big')  # Convert message to integer
        encrypted_message = encrypt(public_key, message_int)
        
        # Send encrypted message
        conn.sendall(str(encrypted_message).encode())
        print(f"Encrypted Message sent: {encrypted_message}")
