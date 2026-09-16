import sys

from client.client import Client
from client.gui import GUI


client = Client("127.0.0.1", 4444)
gui = GUI(client)

gui.run()