import socket
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def verify_signature(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def load_public_key(pem_data):
    return serialization.load_pem_public_key(
        pem_data,
        backend=default_backend()
    )

def send_message(host='localhost', port=12345, message=b'Hello, this is a signed message!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Send message to the server
        client_socket.sendall(message)

        # Receive public key from the server
        public_key_bytes = client_socket.recv(2048)
        public_key = load_public_key(public_key_bytes)

        # Receive the signature from the server
        signature = client_socket.recv(256)  # Adjust size if necessary

        # Verify the signature
        if verify_signature(message, signature, public_key):
            print("Signature is valid. The message integrity is verified.")
        else:
            print("Signature is invalid. The message integrity is compromised.")

if __name__ == "__main__":
    send_message()
