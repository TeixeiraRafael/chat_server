import sys
import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/disconnect"
SERVER = "127.0.0.1"

ADDR = (SERVER, int(sys.argv[1]))

connected = True

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def parse_message():
    global connected
    while connected: 
        msg = input()
        if(msg == DISCONNECT_MESSAGE):
            send(msg)
            print("Exiting...")
            connected = False
        else:
            send(msg)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

thread = threading.Thread(target=parse_message)
thread.start()

while connected:
    print(client.recv(2048).decode(FORMAT))

