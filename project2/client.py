# Import the socket module to enable network communication
import socket
# Importing threading module to handle multiple clients simultaneously
import threading


# A function to handle receiving messages from the server
# It receives sock - the socket object used for communication with the server
def receive_messages(sock):
    # This function runs in a loop to continuously receive messages from the server
    # It will print any messages received from the server to the console
    while True:
        try:
            # Receive data from the server
            data = sock.recv(1024)

            # If no data is received, it means the server has closed the connection
            if not data:
                print("[INFO] Server closed the connection.")
                break

            # Decode the received bytes back into a string and print it
            print(data.decode('ascii'))

        except Exception as e:
            # If an error occurs while receiving data, print the error message
            # This could happen if the server is down or if there is a network issue
            print(f"[ERROR] Receiving message: {e}")
            break


# This function sends messages to the server
# It takes sock - the socket object used for communication with the server and nick - the user's nickname
def send_messages(sock, nick):
    while True:
        try:
            # Prompt the user for input
            message = input()

            # If the user types '/quit', close the socket and exit the loop
            if message.lower() == '/quit':
                print("[INFO] Disconnecting from server.")
                sock.close()
                break

            # Combine the nickname and message into a single string
            full_message = f"{nick} : {message}"
            # Send the message to the server encoded as ASCII
            sock.send(full_message.encode('ascii'))

        except Exception as e:
            # If an error occurs while sending data, print the error message
            print(f"[ERROR] Sending message: {e}")
            break


# The function that will handle communication with the server
def Main():
    # Define the host and port for the server connection
    host = '127.0.0.1'
    port = 12345

    # Create a socket object using IPv4 and TCP
    # AF_INET for Internet Protocol version 4
    # SOCK_STREAM for Transmission Control Protocol
    # This socket will be used to connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server using the specified host and port
    s.connect((host, port))

    # Prompt the user for their nickname
    nick = input("Enter your nickname: ")
    print("Connected! Type your messages below. Type `/quit` to exit.")

    # Start receiving messages in a separate thread
    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()

    # Handle sending messages in the main thread
    send_messages(s, nick)




# Check if the script is being run directly (not imported)
# If so, call the main function to start the client
if __name__ == '__main__':
    Main()
