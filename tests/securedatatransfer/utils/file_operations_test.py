import os
import pytest
from unittest.mock import patch
from src.securedatatransfer.utils.file_operations import (
    read_file,
    write_file,
    get_file_size,
    get_encrypted_file_path,
    get_decrypted_file_path,
    select_file,
    select_directory,
    get_file_name,
)

# Mock data and paths
original_file_path = "assets/test/encrypted/test.txt"
encrypted_file_path = "assets/test/encrypted/test.txt.enc"
temp_directory = "assets/temp"
test_data = b"Test data for writing."


@pytest.fixture
def setup_file(tmpdir):
    """Fixture to set up and tear down a temporary file."""
    file = tmpdir.join("testfile.txt")
    file.write_binary(test_data)
    yield str(file)


def test_read_file(setup_file):
    """Test reading from a file."""
    content = read_file(setup_file)
    assert content == test_data


def test_write_file(tmpdir):
    """Test writing to a file."""
    file_path = tmpdir.join("write_test.txt")
    write_file(str(file_path), test_data)
    assert file_path.read_binary() == test_data


def test_get_file_size(setup_file):
    """Test getting file size."""
    size = get_file_size(setup_file)
    assert size == len(test_data)


def test_get_encrypted_file_path():
    """Test generating encrypted file path."""
    encrypted_path = get_encrypted_file_path(original_file_path)
    assert encrypted_path == encrypted_file_path


def test_get_decrypted_file_path():
    """Test generating decrypted file path."""
    decrypted_path = get_decrypted_file_path(encrypted_file_path)
    assert decrypted_path == original_file_path


@patch("PyQt5.QtWidgets.QFileDialog.getOpenFileName")
def test_select_file(mock_get_open_file_name):
    """Test file selection dialog."""
    mock_get_open_file_name.return_value = (original_file_path, None)
    selected_file = select_file()
    assert selected_file == original_file_path


@patch("PyQt5.QtWidgets.QFileDialog.getExistingDirectory")
def test_select_directory(mock_get_existing_directory):
    """Test directory selection dialog."""
    mock_get_existing_directory.return_value = temp_directory
    selected_directory = select_directory()
    assert selected_directory == temp_directory


def test_get_file_name():
    """Test extracting file name from path."""
    file_name = get_file_name(original_file_path)
    assert file_name == "test.txt"