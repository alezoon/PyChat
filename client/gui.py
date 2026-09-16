from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser, QLineEdit
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import sys

class GUI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()

        self.file = QFile("./bin/main.ui")
        self.file.open(QFile.ReadOnly)

        self.window = self.loader.load(self.file)
        self.file.close()

        if self.window is None:
            raise RuntimeError("Failed to load main.ui")


    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    gui = GUI()
    gui.run()