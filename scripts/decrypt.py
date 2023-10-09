import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QDesktopWidget, QHBoxLayout, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

MAX_RSA_BLOCK_SIZE = 256


class DecryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Decryption')
        self.setGeometry(0, 0, 450, 250)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel('Select an encrypted file to decrypt', self)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        select_button = QPushButton('Select Encrypted File', self)
        layout.addWidget(select_button, alignment=Qt.AlignCenter)
        select_button.clicked.connect(self.selectFile)

        self.encryption_type_combo = QComboBox(self)
        self.encryption_type_combo.addItem(
            "{ Select the Encryption Algorithm }")
        self.encryption_type_combo.addItem("Symmetric Encryption (AES)", 1)
        self.encryption_type_combo.addItem("Asymmetric Encryption (RSA)", 2)
        layout.addWidget(self.encryption_type_combo, alignment=Qt.AlignCenter)

        self.key_label = QLabel('Enter Decryption Key:', self)
        layout.addWidget(self.key_label, alignment=Qt.AlignCenter)

        self.key_input = QLineEdit(self)
        layout.addWidget(self.key_input, alignment=Qt.AlignCenter)

        self.key_select_button = QPushButton(
            'Select Private Key File', self)
        layout.addWidget(self.key_select_button, alignment=Qt.AlignCenter)
        self.key_select_button.clicked.connect(self.selectPrivateKey)

        self.private_key_label = QLabel('', self)
        layout.addWidget(self.private_key_label, alignment=Qt.AlignCenter)

        decrypt_button = QPushButton('Decrypt', self)
        layout.addWidget(decrypt_button, alignment=Qt.AlignCenter)
        decrypt_button.clicked.connect(self.decryptFile)

        self.selected_file = None
        self.selected_private_key = None

        # Initially, hide the key input and select private key button
        self.key_label.hide()
        self.key_input.hide()
        self.key_select_button.hide()
        self.private_key_label.hide()

        self.encryption_type_combo.currentIndexChanged.connect(
            self.updateKeyInputUI)

    def updateKeyInputUI(self):
        selected_method_id = self.encryption_type_combo.currentData()

        if selected_method_id == 1:  # Symmetric Encryption
            self.key_input.show()
            self.key_label.show()
            self.key_select_button.hide()
            self.private_key_label.hide()
        elif selected_method_id == 2:  # Asymmetric Encryption
            self.key_label.hide()
            self.key_input.hide()
            self.key_select_button.show()
            self.private_key_label.show()

    def selectFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Encrypted File", "", "All Files (*);;Encrypted Files (*.enc)", options=options)

        if file_path:
            self.selected_file = file_path
            self.label.setText(f"Selected File: {os.path.basename(file_path)}")

    def selectPrivateKey(self):
        options = QFileDialog.Options()
        private_key_file, _ = QFileDialog.getOpenFileName(
            self, "Select Private Key File", "", "All Files (*);;Private Key Files (*.pem)", options=options)

        if private_key_file:
            self.selected_private_key = private_key_file
            self.private_key_label.setText(
                f"Selected Private Key: {os.path.basename(private_key_file)}")

    def decryptFile(self):
        if self.selected_file:
            selected_method_id = self.encryption_type_combo.currentData()
            decryption_key = self.key_input.text()

            if selected_method_id == 1:
                # Symmetric decryption using AES
                decrypted_data = self.symmetricDecryptAES(
                    self.selected_file, decryption_key)
            elif selected_method_id == 2:
                # Asymmetric decryption using RSA
                decrypted_data = self.asymmetricDecryptRSA(
                    self.selected_file, self.selected_private_key)
            else:
                QMessageBox.warning(
                    self, 'Invalid Encryption Type', 'Please select a valid encryption type.')
                return

            if decrypted_data is not None:
                # Prompt the user to choose a directory to save the decrypted file
                options = QFileDialog.Options()
                directory = QFileDialog.getExistingDirectory(
                    self, "Select Directory to Save Decrypted File", options=options)

                if directory:
                    original_filename = os.path.basename(self.selected_file)
                    save_path = os.path.join(
                        directory, original_filename[:-4])  # Remove ".enc" extension

                    with open(save_path, 'wb') as decrypted_file:
                        decrypted_file.write(decrypted_data)
                    QMessageBox.information(
                        self, 'Decryption Complete', f'File saved to {save_path} successfully.')
                    self.close()  # Close the window after decryption

        else:
            QMessageBox.warning(
                self, 'File Not Selected', 'Please select an encrypted file for decryption.')


    def symmetricDecryptAES(self, encrypted_file_path, key):
        try:
            key = bytes.fromhex(key)
            with open(encrypted_file_path, 'rb') as file:
                nonce = file.read(16)
                ciphertext = file.read()

            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            decrypted_data = cipher.decrypt(ciphertext)
            return decrypted_data
        except Exception as e:
            QMessageBox.warning(
                self, 'Decryption Error', 'Error occurred during decryption: {}'.format(str(e)))
            return None

    def asymmetricDecryptRSA(self, encrypted_file_path, private_key_file):
        try:
            # Load the private key
            with open(private_key_file, 'rb') as key_file:
                private_key_data = key_file.read()
                private_key = RSA.import_key(private_key_data)

            # Read the encrypted file content
            with open(encrypted_file_path, 'rb') as file:
                encrypted_data = file.read()

            # Initialize the RSA cipher with the private key
            cipher_rsa = PKCS1_OAEP.new(private_key)

            # Initialize a buffer for the decrypted data
            decrypted_data = bytearray()

            # Decrypt the file content using RSA in blocks
            for i in range(0, len(encrypted_data), MAX_RSA_BLOCK_SIZE):
                block = encrypted_data[i:i + MAX_RSA_BLOCK_SIZE]
                decrypted_block = cipher_rsa.decrypt(block)
                decrypted_data.extend(decrypted_block)

            return bytes(decrypted_data)
        except Exception as e:
            # Print the exception to identify the issue
            print(f"Decryption Error: {str(e)}")
            return None


def main():
    app = QApplication(sys.argv)
    window = DecryptionApp()

    screen = QDesktopWidget().screenGeometry()
    window_size = window.geometry()
    x = (screen.width() - window_size.width()) // 2
    y = (screen.height() - window_size.height()) // 2
    window.move(x, y)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
