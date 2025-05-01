import socket
import threading

# Server configuration
host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

print("Server is running and listening...")

# Broadcast message to all clients
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Handle incoming messages from a client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))  # Print received message in server terminal
            broadcast(message, sender_socket=client)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                broadcast(f"{username} has left the chat.".encode('utf-8'))
                usernames.remove(username)
            break

# Accept new client connections
def receive_connections():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username is {username}")
        broadcast(f"{username} joined the chat!".encode('utf-8'))
        client.send("Connected to the server.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Server can type messages too
def server_input():
    while True:
        msg = input("")  # Server types here
        broadcast(f"Server: {msg}".encode('utf-8'))

# Start both threads: one for clients, one for server input
threading.Thread(target=receive_connections).start()
threading.Thread(target=server_input).start()
