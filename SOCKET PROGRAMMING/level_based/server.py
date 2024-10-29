import socket
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from ecdsa import SigningKey, VerifyingKey, NIST384p

# Generate ECC keys for Commander
def generate_ecc_keys():
    sk = SigningKey.generate(curve=NIST384p)
    vk = sk.get_verifying_key()
    return sk, vk

# Generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Sign Level 1 data using ECC
def sign_l1(private_key, data):
    return private_key.sign(data.encode())

# Verify Level 1 data using ECC
def verify_l1(public_key, signature, data):
    try:
        public_key.verify(signature, data.encode())
        return True
    except Exception:
        return False

# Read message from file
def read_message_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Encrypt Level 2 data using RSA
def encrypt_l2(public_key, data):
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Decrypt Level 2 data using RSA
def decrypt_l2(private_key, encrypted_data):
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

# Main server function
def main():
    ecc_sk, ecc_vk = generate_ecc_keys()
    rsa_sk, rsa_vk = generate_rsa_keys()

    # Read L1 data from file
    filename = 'message1.txt'
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return

    level_1_data = read_message_from_file(filename)

    # Sign L1 data
    l1_signature = sign_l1(ecc_sk, level_1_data)

    # Level 2 data
    level_2_data = "This is Level 2 public data."

    # Encrypt Level 2 data
    l2_encrypted = encrypt_l2(rsa_vk, level_2_data)
    print("Level 2 data encrypted:", l2_encrypted)  # Display encrypted message

    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("Server listening on port 65432...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            role = conn.recv(1024).decode()
            conn.sendall(f"Role received: {role}".encode())

            if role == "commander":
                conn.sendall(b"Do you want to read Level 1 data? (yes/no)")
                read_l1_response = conn.recv(1024).decode()
                if read_l1_response.lower() == "yes":
                    conn.sendall(level_1_data.encode())
                    l1_decrypt_status = verify_l1(ecc_vk, l1_signature, level_1_data)
                    conn.sendall(f"Level 1 data verification successful: {l1_decrypt_status}".encode())
                else:
                    conn.sendall(b"Access to Level 1 data denied.")

            elif role == "personnel":
                conn.sendall(b"Level 2 data is accessible to you.")
                conn.sendall(l2_encrypted)  # Send encrypted Level 2 data
                print("Sent encrypted Level 2 data to personnel.")
                
                # For demonstration, decrypt Level 2 data and show
                decrypted_l2 = decrypt_l2(rsa_sk, l2_encrypted)
                print("Level 2 data decrypted:", decrypted_l2)

            else:
                conn.sendall(b"Invalid role. Please enter 'commander' or 'personnel'.")
        finally:
            conn.close()

if __name__ == "__main__":
    main()
