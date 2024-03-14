from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QMessageBox,
    QProgressDialog,
    QProgressBar,
    QDesktopWidget,
)
from PyQt5.QtCore import Qt
import time
from ..encryption.symmetric import encrypt_aes
from ..encryption.asymmetric import encrypt_rsa
from ..utils import file_operations as fo
from PyQt5.QtCore import QObject, pyqtSignal, QThread


class EncryptionWorker(QObject):
    encryptionComplete = pyqtSignal(
        str, str
    )
    encryptionFailed = pyqtSignal(str)

    def __init__(self, method, filePath, directory=None, publicKeyPath=None):
        super().__init__()
        self.method = method
        self.filePath = filePath
        self.directory = directory
        self.publicKeyPath = publicKeyPath

    def run(self):
        try:
            if self.method == "aes":
                key, encrypted_file_path = encrypt_aes(self.filePath, self.directory)
                self.encryptionComplete.emit(key, encrypted_file_path)
            elif self.method == "rsa":
                encrypted_file_path = encrypt_rsa(
                    self.filePath, self.publicKeyPath, self.directory
                )
                self.encryptionComplete.emit("", encrypted_file_path)  # No key for RSA
        except Exception as e:
            self.encryptionFailed.emit(str(e))


class EncryptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sending a File")
        self.setGeometry(100, 100, 400, 200)
        self.selectedFilePath = ""
        self.initUI()
        self.centerWindow()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(f"\t\tChoose an encryption method")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItem("Select Sharing Method", "select")
        self.combo.addItem("Group Share", "aes")
        self.combo.addItem("Individual Share", "rsa")
        layout.addWidget(self.combo)

        self.fileButton = QPushButton("Choose File")
        self.fileButton.clicked.connect(self.chooseFile)
        layout.addWidget(self.fileButton)

        self.progressBar = QProgressBar(self)
        self.progressBar.setVisible(False)
        layout.addWidget(self.progressBar)

        self.encryptButton = QPushButton("Encrypt")
        self.encryptButton.clicked.connect(self.encryptFile)
        layout.addWidget(self.encryptButton)

        self.setLayout(layout)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def chooseFile(self):
        filePath = fo.select_file("Select File to Share")
        if filePath:
            self.selectedFilePath = filePath
            self.fileButton.setText("Selected file: " + fo.get_file_name(filePath))

    def encryptFile(self):
        method = self.combo.currentData()
        if method == "select":
            QMessageBox.warning(
                self, "Sharing Method Not Selected", "Please select a sharing method."
            )
            return

        if self.selectedFilePath == "":
            QMessageBox.warning(
                self, "File Not Selected", "Please choose a file to share."
            )
            return

        directory = None
        publicKeyPath = None

        if method == "aes":
            QMessageBox.information(self, "", "Choose where to store the encrypted file to share")
            directory = fo.select_directory()
        elif method == "rsa":
            QMessageBox.information(self, "", "Select your public key")
            publicKeyPath = fo.select_file(
                "Select Public Key", "Public Key Files (*.pem);;"
            )
            if publicKeyPath:
                QMessageBox.information(
                    self, "", "Choose where to save the encrypted file"
                )
                directory = fo.select_directory()

        if directory:
            self.startEncryption(method, directory, publicKeyPath)

    def startEncryption(self, method, directory, publicKeyPath=None):
        self.thread = QThread()
        self.worker = EncryptionWorker(
            method, self.selectedFilePath, directory, publicKeyPath
        )
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.encryptionComplete.connect(self.onEncryptionComplete)
        self.worker.encryptionFailed.connect(self.onEncryptionFailed)

        self.progressBar.setVisible(True)
        self.progressBar.setRange(0, 0)  # Indeterminate progress bar

        self.thread.start()

    def onEncryptionComplete(self, key, encrypted_file_path):
        self.progressBar.setVisible(False)
        if key:  # Show the key for AES encryption
            QMessageBox.information(self, "Encryption Key", f"Encryption key: {key}\n")
        QMessageBox.information(
            self,
            "Encryption Successful",
            f"File has been encrypted successfully.\n\n Encrypted file path: {encrypted_file_path}",
        )
        self.thread.quit()
        self.thread.wait()
        self.accept()

    def onEncryptionFailed(self, error_message):
        QMessageBox.critical(self, "Encryption Failed", error_message)
        self.progressBar.setVisible(False)
        self.thread.quit()
        self.thread.wait()