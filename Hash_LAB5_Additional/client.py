import socket
import hashlib
import time

def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

def send_data(host='localhost', port=12345, message=b'This is a message sent in parts.'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Split the message into parts
        parts = [message[i:i + 10] for i in range(0, len(message), 10)]

        # Send each part with a small delay
        for part in parts:
            print(f"Sending part: {part}")
            client_socket.sendall(part)
            time.sleep(1)  # Optional delay to simulate real-world transmission

        # Close the connection to indicate the end of transmission
        client_socket.shutdown(socket.SHUT_WR)

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
