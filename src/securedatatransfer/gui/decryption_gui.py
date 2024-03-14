from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QDesktopWidget,
    QApplication,
)
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from ..decryption.symmetric import decrypt_aes
from ..decryption.asymmetric import decrypt_rsa
from ..utils import file_operations as fo


class DecryptionWorker(QObject):
    decryptionComplete = pyqtSignal(str)
    decryptionFailed = pyqtSignal(str)

    def __init__(self, method, filePath, key, privateKeyPath, directory):
        super().__init__()
        self.method = method
        self.filePath = filePath
        self.key = key
        self.privateKeyPath = privateKeyPath
        self.directory = directory

    def run(self):
        try:
            if self.method == "aes":
                decrypted_file_path = decrypt_aes(
                    self.filePath, self.key, self.directory
                )
            elif self.method == "rsa":
                decrypted_file_path = decrypt_rsa(
                    self.filePath, self.privateKeyPath, self.directory
                )
            else:
                raise ValueError("Invalid decryption method.")
            self.decryptionComplete.emit(decrypted_file_path)
        except Exception as e:
            self.decryptionFailed.emit(str(e))


class DecryptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Decrypt File")
        self.setGeometry(100, 100, 400, 300)
        self.selectedFilePath = ""
        self.privateKeyPath = ""
        self.initUI()
        self.centerWindow()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(f"\t\tChoose decryption method")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItem("Select Method", "select")
        self.combo.addItem("Group Share", "aes")
        self.combo.addItem("Individual Share", "rsa")
        layout.addWidget(self.combo)

        self.combo.currentIndexChanged.connect(self.onMethodChange)

        self.fileButton = QPushButton("Choose Encrypted File")
        self.fileButton.clicked.connect(self.chooseFile)
        layout.addWidget(self.fileButton)

        self.keyInput = QLineEdit()
        self.keyInput.setPlaceholderText("Enter The Decryption Key")
        self.keyInput.setVisible(False)
        layout.addWidget(self.keyInput)

        self.privateKeyButton = QPushButton("Select Your Private Key File")
        self.privateKeyButton.clicked.connect(self.selectPrivateKey)
        self.privateKeyButton.setVisible(False)
        layout.addWidget(self.privateKeyButton)

        self.progressBar = QProgressBar(self)
        self.progressBar.setVisible(False)
        layout.addWidget(self.progressBar)

        self.decryptButton = QPushButton("Decrypt")
        self.decryptButton.clicked.connect(self.decryptFile)
        layout.addWidget(self.decryptButton)

        self.setLayout(layout)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onMethodChange(self):
        method = self.combo.currentData()
        self.keyInput.setVisible(method == "aes")
        self.privateKeyButton.setVisible(method == "rsa")

    def chooseFile(self):
        filePath = fo.select_file("Select Encrypted File", "Encrypted Files (*.enc);;")
        if filePath:
            self.selectedFilePath = filePath
            self.fileButton.setText("Selected file: " + fo.get_file_name(filePath))

    def selectPrivateKey(self):
        privateKeyPath = fo.select_file(
            "Select Private Key File", "Private Key Files (*.pem);;"
        )
        if privateKeyPath:
            self.privateKeyPath = privateKeyPath
            self.privateKeyButton.setText(
                "Selected key: " + fo.get_file_name(privateKeyPath)
            )

    def decryptFile(self):
        method = self.combo.currentData()
        if method == "select":
            QMessageBox.warning(self, "Error", "Please select a sharing method.")
            return

        if self.selectedFilePath == "":
            QMessageBox.warning(
                self, "File Not Selected", "Please choose the shared file."
            )
            return

        key = self.keyInput.text() if method == "aes" else None
        privateKeyPath = self.privateKeyPath if method == "rsa" else None
        if method == "aes" and not key or method == "rsa" and not privateKeyPath:
            QMessageBox.information(
                self, "Provide decryption key", "Please provide the decryption key."
            )
            return
        QMessageBox.information(
                self, "Select a directory", "Select a directory to store the decrypted file."
            )
        directory = fo.select_directory("Choose where to save the decrypted file")
        if not directory:
            QMessageBox.warning(
                self, "Error", "Please select a directory to save the decrypted file."
            )
            return
        self.progressBar.setVisible(True)
        self.progressBar.setRange(0, 0)

        self.startDecryption(
            method, self.selectedFilePath, key, privateKeyPath, directory
        )

    def startDecryption(self, method, filePath, key, privateKeyPath, directory):
        self.thread = QThread()
        self.worker = DecryptionWorker(method, filePath, key, privateKeyPath, directory)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.decryptionComplete.connect(self.onDecryptionComplete)
        self.worker.decryptionFailed.connect(self.onDecryptionFailed)

        self.thread.start()

    def onDecryptionComplete(self, decrypted_file_path):
        self.progressBar.setVisible(False)
        QMessageBox.information(
            self,
            "Decryption Successful",
            f"File has been decrypted successfully.\n\nStored file path: {decrypted_file_path}",
        )
        self.thread.quit()
        self.thread.wait()
        self.accept()

    def onDecryptionFailed(self, error_message):
        self.progressBar.setVisible(False)
        QMessageBox.critical(self, "Decryption Failed", error_message)
        self.thread.quit()
        self.thread.wait()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dlg = DecryptionDialog()
    dlg.show()
    sys.exit(app.exec_())