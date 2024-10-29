import socket


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port
    host = '10.0.56.53'  # Localhost
    port = 4444

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening for connections
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    # Accept the connection from the client
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Start exchanging messages
    while True:
        # Receive the message from the client
        message = conn.recv(4444).decode() 
        print(f"Client: {message}")

        # Send a response back to the client
        server_message = input("You: ")
        conn.send(server_message.encode())
        if server_message.lower() == 'exit':
            break

    # Close the connection
    conn.close()
    server_socket.close()


if _name_ == "_main_":
    start_server()