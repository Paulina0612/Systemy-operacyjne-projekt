# Import the socket library for creating server/client communication
import socket

# Importing thread functionality from _thread module for handling multiple clients
from _thread import *
import threading

# A lock object to manage access to shared resources between threads
# Works as a synchronization primitive to prevent accessing shared data simultaneously
# This is used to ensure that only one thread can access the shared resource at a time
print_lock = threading.Lock()


# This is the function that will handle communication with a connected client
# It takes a client socket object as an argument and processes messages from the client
def threaded_client(c):
    # A loop to keep the thread running for continuous communication
    while True:
        # Receive data from the client (up to 1024 bytes)
        data = c.recv(1024)

        # If no data is received, the client has likely disconnected
        if not data:
            print('Bye')

            # Release the lock so another thread can take it
            print_lock.release()
            break

        # Reverse the received data (assumed to be a string or bytes)
        data = data[::-1]

        # Send the reversed data back to the client
        c.send(data)

    # Close the client connection when done
    c.close()


# This function sets up the main server logic
def main():
    # Empty string means the server will accept connections on all available IPv4 interfaces
    host = ""

    # Define the port on which the server will listen for incoming connections
    port = 12345

    # Create a socket object using 
    # IPv4 (AF_INET for Internet Protocol version 4)
    # and TCP (SOCK_STREAM for Transmission Control Protocol)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    s.bind((host, port))

    # Run an infinite loop to accept multiple client connections
    while True:
        # Accept a new connection from a client
        c, addr = s.accept()

        # Acquire the lock to indicate this thread is handling a client
        print_lock.acquire()

        # Print the address of the connected client
        # addr[0] is the IP address, addr[1] is the port number
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread to handle this client using the threaded() function
        start_new_thread(threaded_client, (c,))


# Entry point of the program; only runs if the script is executed directly
if __name__ == '__main__':
    main()
