# Import the socket library for creating server/client communication
import socket

# Importing threading module to handle multiple clients simultaneously 
import threading

# A lock object to manage access to shared resources between threads
# Works as a synchronization primitive to prevent accessing shared data simultaneously
# This is used to ensure that only one thread can access the shared resource at a time
print_lock = threading.Lock()

# Array to hold client threads
client_sockets = []


# This is the function that will handle communication with a connected client
# It takes a client socket object as an argument and processes messages from the client
def threaded_client(c, addr):
    # Print the address of the connected client
    with print_lock:
        print(f"[{threading.current_thread().name}] Connected to: {addr[0]}:{addr[1]}")

    try:
        # Send a welcome message to the client
        welcome_message = "Welcome to the server! You can start sending messages."
        c.send(welcome_message.encode('ascii'))

        # A loop to keep the thread running for continuous communication
        while True:
            # Receive data from the client (up to 1024 bytes)
            data = c.recv(1024)

            # If no data is received, the client has likely disconnected
            if not data:
                break

            #c.send(data)  # Echo data back to the client
            # Print the received data to the console for all connected clients
            for socket in client_sockets:
                try:
                    # Send the received data to all connected clients
                    socket.send(data)
                except Exception as e:
                    with print_lock:
                        print(f"[{threading.current_thread().name}] Error sending data: {e}")
                

    except Exception as e:
        with print_lock:
            print(f"[{threading.current_thread().name}] Error: {e}")
    finally:
        c.close()
        with print_lock:
            print(f"[{threading.current_thread().name}] Disconnected from: {addr[0]}:{addr[1]}")


# This function sets up the main server logic
def Main():
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
    print("Socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print(f"[MAIN] Server listening on port {port}...")

    while True:
        c, addr = s.accept()
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=threaded_client, args=(c, addr))
        client_sockets.append(c)
        client_thread.start()


# Entry point of the program; only runs if the script is executed directly
if __name__ == '__main__':
    Main()

