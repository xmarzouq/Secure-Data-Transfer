import sys, os
import platform
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt


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
        # Use pkg_resources to locate secure_data_transfer.py in the installed package
        # script_path = pkg_resources.resource_filename(
        #     'secureDataTransfer', 'secure_data_transfer.py') --> using pkg_resources
        script_path = os.path.join(os.path.dirname(__file__), 'secure_data_transfer.py')

        # Determine the appropriate Python interpreter to use
        python_executable = 'python' if platform.system() == 'Windows' else 'python3'

        # Run the secure_data_transfer.py script for file encryption
        subprocess.run([python_executable, script_path])

    def decryptFiles(self):
        # Use pkg_resources to locate decrypt.py in the installed package
        # script_path = pkg_resources.resource_filename(
        #     'secureDataTransfer', 'decrypt.py')
        script_path = os.path.join(os.path.dirname(__file__), 'decrypt.py')

        # Determine the appropriate Python interpreter to use
        python_executable = 'python' if platform.system() == 'Windows' else 'python3'

        # Run the decrypt.py script for file decryption
        subprocess.run([python_executable, script_path])


def main():
    app = QApplication(sys.argv)
    window = SecureFileTransferApp()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
