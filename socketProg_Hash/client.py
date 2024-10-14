import socket
import hashlib

def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

def send_data(host='localhost', port=12345, message=b'Hello, this is a test message!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        # Send data to the server
        print(f"Sending data: {message}")
        client_socket.sendall(message)

        # Receive the hash from the server
        received_hash = client_socket.recv(64).decode()
        print(f"Received hash: {received_hash}")

        # Compute the local hash
        local_hash = compute_hash(message)
        print(f"Computed local hash: {local_hash}")

        # Verify the integrity of the data
        if received_hash == local_hash:
            print("Data integrity verified: Hashes match!")
        else:
            print("Data integrity compromised: Hashes do not match!")

if __name__ == "__main__":
    send_data()
