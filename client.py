import socket

def multiply(number1, number2):
    return number1 * number2;

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
    # the SOCK_STREAM parameter is used so we can use TCP, AF_INET is so we can use IPv4

    host = '10.0.56.53'  # Define the host and port, this uses the host's ip and port
    port = 4444
    client_socket.connect((host, port)) # we use the host and port to connect to the server
    print("Connected to the server!")

    while True:   # We'll continue an infinite loop until one of us disconnects
        client_message = input("You: ") #this takes the message input
        client_socket.send(client_message.encode()) #then sends it to the other user in byte format
        if client_message.lower() == 'exit':
            break
        # Receive the response from the server
        message = client_socket.recv(4444).decode()
        #when the client receives the message, we must decode it from bytes to text
        if message.lower() == 'exit':
            #if the message sent was a prompt to exit the program, then we stop
            print("Server disconnected.")
            break
        print(f"Server: {message}") #otherwise we get the message as normal.

    client_socket.close() # This closes the connection

if __name__ == "__main__":
    start_client() #runs the client function
