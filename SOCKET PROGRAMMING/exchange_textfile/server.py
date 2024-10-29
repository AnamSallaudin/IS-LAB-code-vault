import socket

def send_file(filename):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('localhost', 65432)  # Use localhost and port 65432
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Waiting for a connection...")
    
    while True:
        # Accept a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            
            # Open the file to send
            with open(filename, 'rb') as file:
                print("Sending file...")
                # Read the file and send its content
                while chunk := file.read(1024):
                    connection.sendall(chunk)
                print("File sent successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    send_file("example.txt")  # Change "example.txt" to the file you want to send
