import os
from PyQt5.QtWidgets import QFileDialog

def read_file(file_path, mode='rb'):
    """Reads content from a file."""
    with open(file_path, mode) as file:
        return file.read()

def write_file(file_path, data, mode='wb'):
    """Writes content to a file."""
    with open(file_path, mode) as file:
        file.write(data)

def get_encrypted_file_path(original_path):
    """Generates a file path for saving an encrypted file."""
    directory, filename = os.path.split(original_path)
    return os.path.join(directory, filename + '.enc')

def get_decrypted_file_path(encrypted_path):
    """Generates a file path for saving a decrypted file, removing .enc."""
    directory, filename = os.path.split(encrypted_path)
    return os.path.join(directory, filename.replace('.enc', ''))

def select_file(dialog_title="Select a file", file_filter="All Files (*)"):
    """
    Opens a file dialog to select a file to open.
    
    :param dialog_title: Title of the file dialog window.
    :param file_filter: Filter for the file dialog.
    :return: The selected file path.
    """

    filePath, _ = QFileDialog.getOpenFileName(caption=dialog_title, filter=file_filter)
    return filePath

def select_directory(dialog_title="Select Directory"):
    """
    Opens a directory dialog to select a directory.
    
    :param dialog_title: Title of the directory dialog window.
    :return: The selected directory path.
    """

    directory = QFileDialog.getExistingDirectory(caption=dialog_title)
    return directory

def get_file_name(file_path):
    """
    Extracts the file name from a file path.
    
    :param file_path: Full path to the file.
    :return: The file name.
    """
    return os.path.basename(file_path)