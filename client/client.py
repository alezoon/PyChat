import socket
import threading

class ChatClient:
    def __init__(self, ip: str, port: int):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))

    def send_message(self, message: str):
        self.client.send(message.encode())

    def receive(self):
        return self.client.recv(1024).decode()

    def close(self):
        self.client.close()
