import socket
import threading
from PySide6.QtCore import QObject, Signal

class Client(QObject):

    # Signals
    message_rec = Signal(str)
    disconnected = Signal()
    error = Signal(str)


    def __init__(self, ip: str, port: int):
        super().__init__()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))

        self.running = True

        self.receive_thread = threading.Thread(
            target=None
        )


    def send_message(self, message: str):
        self.client.sendall(message.encode())

    def _recieve_loop(self):
        while self.running:
            try:
                message = self.client.recv(1024)

                if not message:
                    break

                self.message_rec.emit(
                    message.decode()
                )

            except OSError as e:
                if self.running:
                    self.error.emit(str(e))
                break

        self.disconnect.emit()

    def close(self):
        self.client.close()
