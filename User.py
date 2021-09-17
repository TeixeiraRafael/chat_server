
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/exit"

class User():
    _connected = False
    _conn = None
    _username = ""

    def __init__(self, conn, username="guest"):
        self._conn = conn
        self._username = username

    def disconnect(self):
        self._conn.close()
        self._connected = False

    def update(self, msg):
        try:
            self._conn.send(msg.encode(FORMAT))
        except BrokenPipeError:
            print(f"User {self._username} has disconnected")
            pass

    def handle_message(self):
        msg_length = self._conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = self._conn.recv(msg_length).decode(FORMAT)
            return msg