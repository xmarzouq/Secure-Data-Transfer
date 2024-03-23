import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QFileDialog
)
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from ..decryption.asymmetric import layered_rsa_decrypt
from ..utils import file_operations as fo

class LayeredRSADecryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Encrypted AES Key:"))
        self.encryptedKeyInput = QLineEdit()
        layout.addWidget(self.encryptedKeyInput)
        
        self.selectKeyButton = QPushButton("Select Private Key File(s)")
        self.selectKeyButton.clicked.connect(self.selectPrivateKeyFiles)
        layout.addWidget(self.selectKeyButton)
        
        self.decryptButton = QPushButton("Decrypt AES Key")
        self.decryptButton.clicked.connect(self.decryptAESKey)
        layout.addWidget(self.decryptButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Layered RSA Decryptor')
        self.setGeometry(300, 300, 400, 200)
        
        self.privateKeyPaths = []
        
    def selectPrivateKeyFiles(self):
        keys = fo.select_file("Select Public Key", "Private Key Files (*.pem);;")
        if keys:
            self.privateKeyPaths = keys
            QMessageBox.information(self, 'Selected Key Path: ', f'Key Path:\n {keys}')
    
    def decryptAESKey(self):
        encryptedKeyHex = self.encryptedKeyInput.text()
        if not encryptedKeyHex:
            QMessageBox.warning(self, 'Error', 'Please enter the encrypted AES key in hex format.')
            return
        
        if not self.privateKeyPaths:
            QMessageBox.warning(self, 'Error', 'Please select private key file(s) for decryption.')
            return
        
        try:
            decryptedKeyHex = layered_rsa_decrypt(encryptedKeyHex, self.privateKeyPaths)
            QMessageBox.information(self, 'Decryption Successful', f'Decrypted AES Key (Hex):\n{decryptedKeyHex}')
        except Exception as e:
            QMessageBox.critical(self, 'Decryption Failed', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayeredRSADecryptor()
    ex.show()
    sys.exit(app.exec_())