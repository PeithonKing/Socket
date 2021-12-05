import socket
import json

HEADER = 64
PORT = 5001
SERVER = "192.168.29.114"
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
name = "Aritra's Laptop"

x = input(f"Name? [{name}] ")
if x!="":
    name = x

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send(name)

while True:
    s = input("\nEnter Message: ")
    if s == "":
        print("Didn't send empty message!")
        continue
    send(s)
    if s == DISCONNECT_MESSAGE:
        break