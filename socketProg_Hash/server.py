import socket
import hashlib

def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            print(f"Received data: {data}")

            # Compute hash of received data
            data_hash = compute_hash(data)
            print(f"Computed hash: {data_hash}")

            # Send back the computed hash
            conn.sendall(data_hash.encode())

if __name__ == "__main__":
    start_server()
