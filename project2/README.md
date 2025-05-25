# Multiple-thread chat server 

## Launching instruction 
1. To launch this program download code to your computer and unzip it. 
2. Launch terminal in folder Systemy-operacyjne-projekt and run command
   ````md
   py ./project2/server.py
   ````
   to run server simulation. 
3. Launch terminal in folder Systemy-operacyjne-projekt and run command
   ````md
   py ./project2/client.py
   ````
   to run client simulation. You can do it as many times as you like.

## Description
The goal was to implement a simulation of a chat server for multiple clients. 

The challenge was to design a strategy that allows all clients to send and receive messages. The problem illustrates issues in concurrent programming, such as resource allocation and synchronization.

## Code explanaition

### Threads
Each client in the code is represented as a thread in an array. Creation of each client in "server.py" is shown below. 

````python
c, addr = s.accept()
# Start a new thread to handle the client
client_thread = threading.Thread(target=threaded_client, args=(c, addr))
with client_sockets_lock:
    client_sockets.append(c)
client_thread.start()
````

Each client also has a thread inside "client.py" code that handles sending and receiving messages. Creation of the thread is shown below. 

````python
# Start receiving messages in a separate thread
threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
````

Sending and receiving messages have their own functions.

### Critical sections
Critical sections are parts of code, where threads have access to shared resources. In the code there are two critical sections.

1. Printing from Threads
   ````python
    with print_lock:
    print(f"[{threading.current_thread().name}] Connected to: {addr[0]}:{addr[1]}")
   ````
   The lock ensures only one thread prints at a time, preserving output clarity.

2. Access to client_sockets
   ````python
   # Safely iterate over clients
    with client_sockets_lock:
        for socket in client_sockets:
            try:
                socket.send(data)
            except Exception as e:
                ...
    ````

