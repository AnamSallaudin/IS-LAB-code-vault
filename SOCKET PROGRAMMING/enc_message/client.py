import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64

# Decrypt message using RSA private key
def decrypt_message(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

def main():
    # Set up the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    # Receive encrypted message
    encrypted_message = client_socket.recv(1024)
    print("Received encrypted message (in bytes):", encrypted_message)

    # Show encrypted message in base64 for readability
    encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')
    print("Encrypted message (base64):", encrypted_message_base64)

    # Receive private key
    pem = client_socket.recv(1024)
    print("Received private key.")

    # Load the private key
    private_key = serialization.load_pem_private_key(
        pem,
        password=None,
        backend=default_backend()
    )

    # Decrypt the message
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
