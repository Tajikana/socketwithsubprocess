import socket

host = "127.0.0.1"
port = 14001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
msg = input("Enter a message: ")

while msg.lower().strip() != "quit":
    if msg != "":
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print("response " + str(data))
    msg = input(">>")
client_socket.close()
