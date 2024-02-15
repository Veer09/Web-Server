import socket

HOST = "127.0.0.1"
PORT = 80

# AF_INET for IPv4 connection and SOCK_STREAM for TCP connection
#Listening Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
#Accepting only one connection at time
socket.listen()

while True:
    #connection:socket which will use to communicate with client
    connection , address = socket.accept()
    data = connection.recv(1024).decode()
    about = data.splitlines()[0]
    path = about.split(' ')[1]
    response = f"HTTP/1.1 200 OK\r\n\r\nRequested path:{path}\r\n"
    connection.sendall(response.encode())
    connection.close()



