import sys
import os
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QDesktopWidget, QComboBox
from PyQt5.QtCore import Qt
import subprocess


class SecureDataTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Secure Data Transfer')
        self.setGeometry(0, 0, 350, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel('Select a file to transfer', self)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        select_button = QPushButton('Select File', self)
        layout.addWidget(select_button, alignment=Qt.AlignCenter)
        select_button.clicked.connect(self.selectFile)

        self.encryption_method_combo = QComboBox(self)
        self.encryption_method_combo.addItem(
            "{ Select the sharing type }")
        self.encryption_method_combo.addItem("Send to a person", 1)
        self.encryption_method_combo.addItem("Send to a group", 2)
        layout.addWidget(self.encryption_method_combo,
                         alignment=Qt.AlignCenter)

        encrypt_button = QPushButton('Encrypt', self)
        layout.addWidget(encrypt_button, alignment=Qt.AlignCenter)
        encrypt_button.clicked.connect(self.encryptAndTransfer)

        self.selected_file = None

    def selectFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if file_path:
            self.selected_file = file_path
            file_name = os.path.basename(self.selected_file)
            self.label.setText(f"Selected File: {file_name} ")

    def encryptAndTransfer(self):
        if self.selected_file:
            selected_method_id = self.encryption_method_combo.currentData()
            if selected_method_id == 1:
                # Implement asymmetric encryption logic using self.selected_file
                self.performAsymmetricEncryption(self.selected_file)
            elif selected_method_id == 2:
                # Implement symmetric encryption logic using self.selected_file
                self.performSymmetricEncryption(self.selected_file)
        else:
            self.label.setText("No file selected for encryption and transfer")

    def performSymmetricEncryption(self, file_path):
        # Use pkg_resources to locate symmetricEncryptAES.py in the installed package
        # script_path = pkg_resources.resource_filename(
        #     'secureDataTransfer', 'symmetricEncryptAES.py')
        script_path = os.path.join(os.path.dirname(__file__), 'symmetricEncryptAES.py')

        # Determine the appropriate Python interpreter to use
        python_executable = 'python' if platform.system() == 'Windows' else 'python3'

        # Call symmetricEncryptAES.py with the selected file path
        result = subprocess.run(
            [python_executable, script_path, file_path], stdout=subprocess.PIPE)

        if result.returncode == 0:
            # Display a message to indicate successful encryption
            self.label.setText("File encrypted successfully.")
            # Close the window after encryption
            self.close()
        else:
            self.label.setText("Error occurred during encryption")

    def performAsymmetricEncryption(self, file_path):
        # Use pkg_resources to locate asymmetricRSAEncrypt.py in the installed package
        # script_path = pkg_resources.resource_filename(
        #     'secureDataTransfer', 'asymmetricRSAEncrypt.py')
        script_path = os.path.join(os.path.dirname(__file__), 'asymmetricRSAEncrypt.py')

        # Determine the appropriate Python interpreter to use
        python_executable = 'python' if platform.system() == 'Windows' else 'python3'

        # Call asymmetricRSAEncrypt.py with the selected file path
        result = subprocess.run(
            [python_executable, script_path, file_path], stdout=subprocess.PIPE)

        if result.returncode == 0:
            # Display a message to indicate successful encryption
            self.label.setText("File encrypted successfully.")
            # Close the window after encryption
            self.close()
        else:
            self.label.setText("Error occurred during encryption")


def main():
    app = QApplication(sys.argv)
    window = SecureDataTransferApp()

    screen = QDesktopWidget().screenGeometry()
    window_size = window.geometry()
    x = (screen.width() - window_size.width()) // 2
    y = (screen.height() - window_size.height()) // 2
    window.move(x, y)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
