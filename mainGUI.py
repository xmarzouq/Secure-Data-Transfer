import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt
import subprocess


class SecureFileTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Secure File Transfer')

        # Set the window dimensions
        window_width = 350
        window_height = 200
        self.setGeometry(0, 0, window_width, window_height)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        encrypt_button = QPushButton('Encrypt Files', self)
        layout.addWidget(encrypt_button, alignment=Qt.AlignCenter)
        encrypt_button.clicked.connect(self.encryptFiles)

        decrypt_button = QPushButton('Decrypt Files', self)
        layout.addWidget(decrypt_button, alignment=Qt.AlignCenter)
        decrypt_button.clicked.connect(self.decryptFiles)

        # Center the window on the screen
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - window_width) // 2
        y = (screen.height() - window_height) // 2
        self.move(x, y)

    def encryptFiles(self):
        # Run the secure_data_transfer.py script for file encryption

        subprocess.run(['python', './scripts/secure_data_transfer.py'])

    def decryptFiles(self):
        # Run the symmetricDecryptAES.py script for file decryption
        subprocess.run(['python', './scripts/decrypt.py'])


def main():
    app = QApplication(sys.argv)
    window = SecureFileTransferApp()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
