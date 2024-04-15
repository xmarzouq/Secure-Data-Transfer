import os
import pytest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from unittest.mock import MagicMock, patch
from src.securedatatransfer.gui.encryption_gui import EncryptionDialog
from src.securedatatransfer.gui.decryption_gui import DecryptionDialog
from src.securedatatransfer.encryption.symmetric import encrypt_aes
from src.securedatatransfer.encryption.asymmetric import encrypt_rsa
from src.securedatatransfer.decryption.asymmetric import decrypt_rsa
from Crypto.PublicKey import RSA

@pytest.fixture(scope='session')
def app():
    """Fixture to manage QApplication lifecycle."""
    app = QApplication([])
    yield app
    app.quit()

@pytest.fixture
def encryption_dialog(qtbot, mocker):
    """Fixture for setting up EncryptionDialog."""
    mocker.patch('PyQt5.QtWidgets.QMessageBox.information')
    mocker.patch('PyQt5.QtWidgets.QMessageBox.warning')
    dialog = EncryptionDialog()
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def decryption_dialog(qtbot, mocker):
    """Fixture for setting up DecryptionDialog."""
    mocker.patch('PyQt5.QtWidgets.QMessageBox.information')
    mocker.patch('PyQt5.QtWidgets.QMessageBox.warning')
    dialog = DecryptionDialog()
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def aes_encryption_data(encryption_dialog, qtbot):
    """Encrypt a temporary file and provide the path and key for other tests."""
    directory = 'tests/temp/AES'
    file_path = os.path.join(directory, 'testfile_aes.txt')
    with open(file_path, 'w') as file:
        file.write('TEST AES DATA...')
    aes_key, encrypted_file_path = encrypt_aes(file_path, directory)

    encryption_dialog.worker = MagicMock()
    encryption_dialog.worker.encryptionComplete.emit(aes_key, encrypted_file_path)

    return {'file_path': encrypted_file_path, 'aes_key': aes_key}

def test_aes_decryption_workflow(qtbot, decryption_dialog, mocker, aes_encryption_data):
    """Test the decryption workflow using encrypted data."""
    encrypted_file_path = aes_encryption_data['file_path']
    aes_key = aes_encryption_data['aes_key']
    decrypted_directory = 'tests/temp/AES/decrypted'
    decrypted_file_path = os.path.join(decrypted_directory, 'testfile_aes.txt')

    mocker.patch('src.securedatatransfer.utils.file_operations.select_file', return_value=encrypted_file_path)
    mocker.patch('src.securedatatransfer.utils.file_operations.select_directory', return_value=decrypted_directory)

    assert os.path.exists(encrypted_file_path), "Encrypted file does not exist"

    qtbot.mouseClick(decryption_dialog.fileButton, Qt.LeftButton)
    decryption_dialog.combo.setCurrentIndex(1)
    decryption_dialog.keyInput.setText(aes_key)
    qtbot.mouseClick(decryption_dialog.decryptButton, Qt.LeftButton)

    qtbot.waitSignal(decryption_dialog.worker.decryptionComplete, timeout=1000)
    decryption_dialog.worker.decryptionComplete.emit(decrypted_file_path)


    assert os.path.exists(decrypted_file_path), "Decrypted file should exist"
    QMessageBox.information.assert_any_call(
        decryption_dialog,
        "Decryption Successful",
        f"File has been decrypted successfully.\n\nStored file path: {decrypted_file_path}"
    )

@pytest.fixture
def rsa_keys(tmp_path):
    """Generate RSA key pair for encryption and decryption and save to temporary files."""
    directory = 'tests/temp/keys/'
    key = RSA.generate(2048)
    private_key_path = os.path.join(directory, "private_key.pem")
    public_key_path = os.path.join(directory, "public_key.pem")
    with open(private_key_path, "wb") as private_file:
        private_file.write(key.export_key())
    with open(public_key_path, "wb") as public_file:
        public_file.write(key.publickey().export_key())
    return {'public_key_path': str(public_key_path), 'private_key_path': str(private_key_path)}

@pytest.fixture
def rsa_encryption_data(tmp_path, rsa_keys):
    """Encrypt a file using RSA and provide the paths for decryption tests."""
    directory = 'tests/temp/RSA'
    file_path = os.path.join(directory, 'testfile_rsa.txt')
    with open(file_path, 'w') as file:
        file.write('TEST RSA DATA...')
    encrypted_file_path = encrypt_rsa(file_path, rsa_keys['public_key_path'], directory)

    return {
        'encrypted_file_path': encrypted_file_path,
        'private_key_path': rsa_keys['private_key_path'],
        'directory': str(directory)
    }

def test_rsa_decryption_workflow(qtbot, decryption_dialog, rsa_encryption_data, mocker):
    """Test the RSA decryption workflow using the encrypted data and private key."""
    encrypted_file_path = rsa_encryption_data['encrypted_file_path']
    private_key_path = rsa_encryption_data['private_key_path']
    decrypted_directory = 'tests/temp/RSA/decrypted'
    decrypted_file_path = os.path.join(decrypted_directory, 'testfile_rsa.txt')

    # Mock the file and directory selection within the dialog
    mocker.patch('src.securedatatransfer.utils.file_operations.select_file', side_effect=[encrypted_file_path, private_key_path])
    mocker.patch('src.securedatatransfer.utils.file_operations.select_directory', return_value=decrypted_directory)

    # Simulate selecting RSA decryption method
    qtbot.mouseClick(decryption_dialog.fileButton, Qt.LeftButton)  # Trigger file selection
    decryption_dialog.combo.setCurrentIndex(2)  # Assuming 3 is RSA; adjust if index is different
    qtbot.mouseClick(decryption_dialog.privateKeyButton, Qt.LeftButton)  # Trigger private key selection
    qtbot.mouseClick(decryption_dialog.decryptButton, Qt.LeftButton)

    # Since actual file operations and decryption are mocked, directly emit the signal
    qtbot.waitSignal(decryption_dialog.worker.decryptionComplete, timeout=1000)
    decryption_dialog.worker.decryptionComplete.emit(decrypted_file_path)

    # Check the final result
    assert os.path.exists(decrypted_file_path), "Decrypted file should exist"
    with open(decrypted_file_path, 'r') as file:
        decrypted_content = file.read()
    assert decrypted_content == 'TEST RSA DATA...', "Decrypted content does not match the original"

    # Verify that the information message was correctly displayed
    QMessageBox.information.assert_any_call(
        decryption_dialog,
        "Decryption Successful",
        f"File has been decrypted successfully.\n\nStored file path: {decrypted_file_path}"
    )


# Teardown function to delete files in the tests/temp/ directory after the test is finished
@pytest.fixture(scope='session', autouse=True)
def cleanup_temp_files():
    yield
    temp_directory = 'tests/temp'
    for root, dirs, files in os.walk(temp_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    pytest.main()