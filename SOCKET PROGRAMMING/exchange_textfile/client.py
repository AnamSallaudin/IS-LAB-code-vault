import socket

def receive_file(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)
    client_socket.connect(server_address)
    
    with open(filename, 'wb') as file:
        print("Receiving file...")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
        print("File received successfully.")

    client_socket.close()

    # Display the contents of the received file
    with open(filename, 'r') as file:
        contents = file.read()
        print("\nContents of the received file:")
        print(contents)

if __name__ == "__main__":
    receive_file("received_example.txt")  # This file will be created

