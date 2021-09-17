import socket
import threading

from User import *

DISCONNECT_MESSAGE = "/exit"
   
class ChatRoom():
    _users = []
    _server = None
    _host = ''
    _port = None
    _addr = None
    _user_count = 0
    _active_connections = 0

    def __init__(self, host='127.0.0.1', port=5050):
        self._host = host
        self._port = port
        self._addr = (self._host, self._port)

    def attach(self, user):
        self._users.append(user)

    def detach(self, user):
        self._users.remove(user)

    def notify(self, msg):
        for user in self._users:
            user.update(msg)

    def handle_user(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        self._active_connections += 1
        if(self._user_count > 0):
            user = User(conn, f"Guest {self._user_count}")
            user._connected = True
            self._user_count += 1
        else:
            user = User(conn, "Guest")
            user._connected = True
            self._user_count += 1

        self.attach(user)

        while user._connected:
            self.parse_message(user)

    def parse_message(self, user):
        msg = user.handle_message()
        if(msg == None):
            return

        if(msg.startswith(DISCONNECT_MESSAGE)):
            self.handle_disconnect(user)
        elif(msg.startswith("/username") and len(msg.split(" ")) >= 2):
            self.handle_username_update(user, msg)
        else:
            self.notify(f"{user._username}:\t{msg}")

    def handle_disconnect(self, user):
        self.detach(user)
        self.notify(f"{user._username} disconnected.")
        print(f"{user._username} disconnected.")
        user.disconnect()
        self._active_connections -= 1

    def handle_username_update(self, user, msg):
        new_name = msg.split(" ")[1]
        if new_name in [user._username for user in self._users]:
            user.update("Username already in use")
        else:
            old_name = user._username
            user._username = new_name
            self.notify(f"{old_name} changed its username to {new_name}")
            

    def start(self):
        print(f"Server is starting")

        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(self._addr)
        self._server.listen()

        while True:
            conn, addr = self._server.accept()
            thread = threading.Thread(target=self.handle_user, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {self._active_connections}")
    

    def __del__(self):
        self._server.close()