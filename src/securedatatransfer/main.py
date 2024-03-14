from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QDesktopWidget,
)
import sys
from .gui.encryption_gui import EncryptionDialog
from .gui.decryption_gui import DecryptionDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Data Transfer")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()
        self.centerWindow()

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)

        encryptionButton = QPushButton("Send a File")
        encryptionButton.clicked.connect(self.openEncryptionDialog)
        layout.addWidget(encryptionButton)

        decryptionButton = QPushButton("Receive a File")
        decryptionButton.clicked.connect(self.openDecryptionDialog)
        layout.addWidget(decryptionButton)

    def openEncryptionDialog(self):
        dialog = EncryptionDialog(self)
        dialog.exec_()

    def openDecryptionDialog(self):
        dialog = DecryptionDialog(self)
        dialog.exec_()

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()