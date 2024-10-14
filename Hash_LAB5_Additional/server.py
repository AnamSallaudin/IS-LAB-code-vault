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
            message_parts = []

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received part: {data}")
                message_parts.append(data)

            # Reassemble the message
            full_message = b''.join(message_parts)
            print(f"Reassembled message: {full_message}")

            # Compute hash of the reassembled message
            message_hash = compute_hash(full_message)
            print(f"Computed hash: {message_hash}")

            # Send back the computed hash
            conn.sendall(message_hash.encode())

if __name__ == "__main__":
    start_server()
