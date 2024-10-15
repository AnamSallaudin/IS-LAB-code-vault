import socket

# RSA Decryption
def decrypt(private_key, public_key, ciphertext):
    d = private_key
    e, n = public_key
    plaintext = pow(ciphertext, d, n)  # m = c^d mod n
    return plaintext

# Client setup
HOST = '127.0.0.1'  # Server address
PORT = 65432        # Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Receive the public key
    public_key_data = client_socket.recv(1024).decode()
    e, n = map(int, public_key_data.split(','))
    public_key = (e, n)
    print(f"Public Key received: {public_key}")
    
    # Receive the private key
    private_key = int(client_socket.recv(1024).decode())
    print(f"Private Key received: {private_key}")

    # Receive the encrypted message
    encrypted_message = client_socket.recv(1024).decode()
    encrypted_message_int = int(encrypted_message)  # Convert received string back to integer
    print(f"Encrypted Message received: {encrypted_message_int}")

    # Decrypt the message
    decrypted_message_int = decrypt(private_key, public_key, encrypted_message_int)
    
    # Convert integer back to string
    decrypted_message_bytes = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, 'big')
    decrypted_message = decrypted_message_bytes.decode()  # Convert bytes back to string
    
    print(f"Decrypted Message: '{decrypted_message}'")
