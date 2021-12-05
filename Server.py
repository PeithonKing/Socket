import socket
import threading
import json

HEADER = 64
PORT = 5001
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = {}

n_connections = 0

def handle_client(conn, addr):
    global clients
    global n_connections
    named = False
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if not named:
                clients[addr] = msg
                named = True
                print(f"{msg} joined!".upper())
            else:
                if msg == DISCONNECT_MESSAGE:
                    n_connections -= 1
                    print(f"{clients[addr]} disconnected".upper())
                    # print(f"Active Connection = {n_connections}\n")
                    connected = False
                else:
                    print(f"[{clients[addr]}] {msg}")
    conn.close()

def start():
    global n_connections
    server.listen()
    print(f"server at {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        n_connections += 1
        print(f"Active Connection = {n_connections}")

print("Server is starting...")
start()