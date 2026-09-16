from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser, QLineEdit
from PySide6.QtCore import QFile, Signal
from PySide6.QtUiTools import QUiLoader
import sys

class GUI:
    def __init__(self, client):

        self.client = client

        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()

        self.file = QFile("./bin/main.ui")
        self.file.open(QFile.ReadOnly)

        self.window = self.loader.load(self.file)
        self.file.close()

        if self.window is None:
            raise RuntimeError("Failed to load main.ui")

        self.client.message_rec.connect(
            self.display_message
        )


    def display_message(self, message):
        self.window.textBrowser.append(message)


    def run(self):
        self.window.show()
        sys.exit(self.app.exec())