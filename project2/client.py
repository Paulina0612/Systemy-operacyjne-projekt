# Import the socket module to enable network communication
import socket


# The function that will handle communication with the server
def Main():
    # Localhost IP address (loopback address) - used to connect to the same machine
    host = '127.0.0.1'

    # Define the port number to connect to
    # Matches the port the server is listening on
    port = 12345

    # Create a socket object using IPv4 addressing (AF_INET)
    # and TCP protocol (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish a connection to the server using the host and port
    s.connect((host, port))

    # User nickname input
    nick = input("Enter your nickname: ")

    # Start a loop to allow repeated communication with the server
    while True:
        # This is the message that will be sent to the server
        message = input("Enter the message: ")

        # Combine the nickname and message into a single string
        # This allows the server to identify who sent the message
        message = nick + ' : ' + message

        # Send the message to the server encoded as ASCII
        # Encoding the message to bytes is necessary for transmission over the network
        s.send(message.encode('ascii'))

        # Receive data from the server
        # The server response is limited to 1024 bytes
        data = s.recv(1024)

        # Decode the received bytes back into a string and print it
        # For example, the server might return the reversed message
        print(str(data.decode('ascii')))

        # Prompt the user to decide whether to continue sending messages
        ans = input('\nDo you want to continue(y/n)? ')

        # If user decides not to continue, exit the loop
        if ans == 'n':
            break
        else:
            # If user chooses to continue, the loop continues
            continue

    # Close the socket connection to clean up resources
    s.close()


# Check if the script is being run directly (not imported)
# If so, call the main function to start the client
if __name__ == '__main__':
    Main()
