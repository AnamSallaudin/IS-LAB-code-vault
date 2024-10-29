import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# Generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Encrypt message using RSA public key
def encrypt_message(public_key, message):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Main server function
def main():
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()

    # Message to encrypt
    message = "Hello, this is a secure message!"

    # Encrypt the message
    encrypted_message = encrypt_message(public_key, message)
    print("Encrypted message:", encrypted_message)

    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("Server listening on port 65432...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            # Send encrypted message
            conn.sendall(encrypted_message)
            print("Sent encrypted message to client.")

            # Send private key (for demonstration only; do not do this in practice)
            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL
            )
            conn.sendall(pem)
            print("Sent private key to client.")
        finally:
            conn.close()

if __name__ == "__main__":
    main()
