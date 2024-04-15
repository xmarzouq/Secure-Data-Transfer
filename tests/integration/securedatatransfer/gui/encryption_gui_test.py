import pytest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from unittest.mock import MagicMock, patch
from src.securedatatransfer.gui.encryption_gui import EncryptionDialog
from Crypto.PublicKey import RSA
import os

@pytest.fixture(scope='session')
def app():
    """Fixture to manage QApplication lifecycle."""
    return QApplication([])

@pytest.fixture
def encryption_dialog(qtbot, mocker, tmp_path):
    """Fixture for setting up EncryptionDialog."""
    mocker.patch('PyQt5.QtWidgets.QMessageBox.information')
    mocker.patch('PyQt5.QtWidgets.QMessageBox.warning')
    dialog = EncryptionDialog()
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def rsa_keys():
    """Generate RSA key pair for each test session."""
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    return {'public_key': public_key, 'private_key': private_key}

def test_rsa_encryption_workflow(qtbot, encryption_dialog, mocker, tmp_path, rsa_keys):
    """Test the RSA encryption workflow simulating all user interactions."""
    file_path = tmp_path / 'testfile.txt'
    file_path.write_text('Dummy data')
    encrypted_file_path = tmp_path / 'testfile.txt.enc'
    public_key_path = tmp_path / 'public_key.pem'
    public_key_path.write_bytes(rsa_keys['public_key'])

    mocker.patch('src.securedatatransfer.utils.file_operations.select_file', side_effect=[str(file_path), str(public_key_path)])
    mocker.patch('src.securedatatransfer.utils.file_operations.select_directory', return_value=str(tmp_path))
    mocker.patch('os.path.getsize', return_value=123)

    qtbot.mouseClick(encryption_dialog.fileButton, Qt.LeftButton)
    encryption_dialog.combo.setCurrentIndex(2)
    qtbot.mouseClick(encryption_dialog.encryptButton, Qt.LeftButton)

    encryption_dialog.worker.encryptionComplete.emit("", str(encrypted_file_path))
    assert os.path.exists(encrypted_file_path), "RSA encrypted file should exist"
    print(QMessageBox.information.call_args_list)


def test_aes_encryption_workflow(qtbot, encryption_dialog, mocker, tmp_path):
    """Test the AES encryption workflow simulating all user interactions."""
    file_path = tmp_path / 'testfile.txt'
    file_path.write_text('Dummy data')
    encrypted_file_path = tmp_path / 'testfile.txt.enc'

    mocker.patch('src.securedatatransfer.utils.file_operations.select_file', return_value=str(file_path))
    mocker.patch('src.securedatatransfer.utils.file_operations.select_directory', return_value=str(tmp_path))
    mocker.patch('os.path.getsize', return_value=123)

    qtbot.mouseClick(encryption_dialog.fileButton, Qt.LeftButton)
    encryption_dialog.combo.setCurrentIndex(1)
    qtbot.mouseClick(encryption_dialog.encryptButton, Qt.LeftButton)

    encryption_dialog.worker.encryptionComplete.emit("", str(encrypted_file_path))
    assert os.path.exists(encrypted_file_path), "Encrypted file should exist"
    print(QMessageBox.information.call_args_list)

    assert any(
        call.args[1] == "Database Update" and "File details added to database successfully." in call.args[2]
        for call in QMessageBox.information.call_args_list
    ), "Expected database update message not shown"

if __name__ == "__main__":
    pytest.main()