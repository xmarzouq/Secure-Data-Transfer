import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QDesktopWidget, QHBoxLayout
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

MAX_RSA_BLOCK_SIZE = 214


class AsymmetricRSAEncryptApp(QMainWindow):

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Asymmetric RSA Encryption')
        # Increased height to accommodate the additional label
        self.setGeometry(0, 0, 400, 250)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a horizontal layout for file label and key label alignment
        label_layout = QHBoxLayout()
        layout.addLayout(label_layout)

        # Create a spacer item to center-align the file label
        label_layout.addStretch()

        file_name = os.path.basename(self.file_path)

        self.file_label = QLabel(f'Selected File: {file_name}', self)
        label_layout.addWidget(self.file_label)

        # Create a spacer item to center-align the file label
        label_layout.addStretch()

        select_key_button = QPushButton('Select Recipient\'s Public Key', self)
        select_key_button.clicked.connect(self.selectRecipientPublicKey)
        layout.addWidget(select_key_button)

        # Create another horizontal layout for the key label alignment
        key_label_layout = QHBoxLayout()
        layout.addLayout(key_label_layout)

        # Create a spacer item to center-align the key label
        key_label_layout.addStretch()

        self.key_label = QLabel('', self)
        key_label_layout.addWidget(self.key_label)

        # Create a spacer item to center-align the key label
        key_label_layout.addStretch()

        encrypt_button = QPushButton('Encrypt', self)
        encrypt_button.clicked.connect(self.encryptFile)
        layout.addWidget(encrypt_button)

        self.recipient_public_key = None

        # Center the main window on the screen
        self.centerOnScreen()

    def centerOnScreen(self):
        # Get the screen's geometry
        screen = QDesktopWidget().screenGeometry()
        # Calculate the center of the screen
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        # Move the window to the center
        self.move(x, y)

    def selectRecipientPublicKey(self):
        options = QFileDialog.Options()
        key_file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Recipient's Public Key File", "", "All Files (*);;Public Key Files (*.pem)", options=options)

        if key_file_path:
            self.recipient_public_key = key_file_path
            # Extract file name from path
            file_name = os.path.basename(key_file_path)
            self.key_label.setText(
                f'Selected Key File: {file_name}')  # Display file name

    def encryptFile(self):
        if not self.recipient_public_key:
            self.key_label.setText(
                "Please select recipient's public key file.")
            return

        try:
            # Load recipient's public key
            with open(self.recipient_public_key, 'rb') as key_file:
                recipient_public_key_data = key_file.read()
                recipient_public_key = RSA.import_key(
                    recipient_public_key_data)

            # Read the file content
            with open(self.file_path, 'rb') as file:
                file_data = file.read()

            # Encrypt the file content using RSA in blocks
            cipher_rsa = PKCS1_OAEP.new(recipient_public_key)

            encrypted_data = b''
            for i in range(0, len(file_data), MAX_RSA_BLOCK_SIZE):
                block = file_data[i:i + MAX_RSA_BLOCK_SIZE]
                encrypted_block = cipher_rsa.encrypt(block)
                encrypted_data += encrypted_block

            # Prompt the user to choose a directory to save the encrypted file
            options = QFileDialog.Options()
            directory = QFileDialog.getExistingDirectory(
                self, "Select Directory to Save Encrypted File", options=options)

            if directory:
                # Create a file name for the encrypted file
                file_name = os.path.basename(self.file_path) + '.enc'
                save_file_path = os.path.join(directory, file_name)

                # Save the encrypted data to the selected file path
                with open(save_file_path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_data)

                # Show a pop-up message indicating successful encryption
                QMessageBox.information(
                    self, "Encryption Successful", f"File encrypted successfully and saved as {file_name}")
                self.close()
        except Exception as e:
            self.key_label.setText(f"Error: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python AsymmetricEncryptRSA.py <file_path>")
        sys.exit(1)

    app = QApplication(sys.argv)
    file_path = sys.argv[1]
    window = AsymmetricRSAEncryptApp(file_path)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
