import socket
import threading

# Connection details
host = '127.0.0.1'
port = 55555

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Get username
username = input("Enter your username: ")

# Receiving messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred. Disconnecting from server.")
            client.close()
            break

# Sending messages
def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))

# Start threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
