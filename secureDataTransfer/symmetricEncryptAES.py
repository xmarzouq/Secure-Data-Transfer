import sys
import os
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget, QDesktopWidget, QLabel, QMessageBox
import pkg_resources  # Import pkg_resources


class SymmetricEncryptionApp(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle('Symmetric Encryption')
        self.setGeometry(0, 0, 350, 200)

        label = QLabel('Choose a directory to store the encrypted file', self)
        layout.addWidget(label)

        select_button = QPushButton('Select Directory', self)
        layout.addWidget(select_button)
        select_button.clicked.connect(self.selectDirectory)

        encrypt_button = QPushButton('Encrypt', self)
        layout.addWidget(encrypt_button)
        encrypt_button.clicked.connect(self.encryptFile)

        self.encryption_key = None
        self.selected_directory = None

        self.setLayout(layout)

    def selectDirectory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory to Store Encrypted File", options=options)
        if directory:
            self.selected_directory = directory

    def encryptFile(self):
        if self.selected_directory:
            # Generate a random 256-bit encryption key
            encryption_key = get_random_bytes(32)

            # Initialize AES cipher with the encryption key
            cipher = AES.new(encryption_key, AES.MODE_EAX)

            # Read the file content
            with open(self.file_path, 'rb') as file:
                file_data = file.read()

            # Encrypt the file data
            ciphertext, tag = cipher.encrypt_and_digest(file_data)

            # Save the encrypted file with .enc extension in the selected directory
            encrypted_file_path = os.path.join(
                self.selected_directory, os.path.basename(self.file_path) + '.enc')
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(cipher.nonce)
                encrypted_file.write(ciphertext)
                encrypted_file.write(tag)

            # Store the encryption key as a hex string
            self.encryption_key = encryption_key.hex()

            # Inform the user
            QMessageBox.information(
                self, 'Encryption Complete', 'File encrypted successfully.')
            if self.encryption_key:
                clipboard = QApplication.clipboard()
                clipboard.setText(self.encryption_key)
                QMessageBox.information(
                    self, 'Key Copied', 'Encryption key copied to clipboard.')
                # Close the window after encryption
                self.close()

        else:
            QMessageBox.warning(
                self, 'Directory Not Selected', 'Please select a directory to store the encrypted file.')


def main():
    app = QApplication(sys.argv)

    # Use pkg_resources to locate the script path within the package
    script_path = pkg_resources.resource_filename(
        'secureDataTransfer', 'SymmetricEncryptAES.py')

    file_path = sys.argv[1]
    window = SymmetricEncryptionApp(file_path)

    # Center the window on the screen
    screen = QDesktopWidget().screenGeometry()
    window_size = window.geometry()
    x = (screen.width() - window_size.width()) // 2
    y = (screen.height() - window_size.height()) // 2
    window.move(x, y)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
