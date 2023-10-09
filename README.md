# SecureDataTransfer

SecureDataTransfer is a Raspberry Pi-based solution for secure and user-friendly data encryption and transfer. It offers robust encryption options and a seamless user experience, making it ideal for protecting sensitive data.

## Overview

The SecureDataTransfer project consists of a combination of software and hardware components:

- **Software Components:**
  - `MainGUI.py`: The main graphical user interface (GUI) for the project. It allows users to choose between encrypting or decrypting files.
  - `Secure_Data_Transfer.py`: Manages the overall workflow, prompting users to select the file, encryption method, and destination directory.
  - `SymmetricEncryptAES.py`: Handles symmetric encryption (group sharing) using the AES algorithm.
  - `AsymmetricRSAEncrypt.py`: Manages asymmetric encryption (individual sharing) using RSA encryption with public keys.
  - `Decrypt.py`: Allows users to decrypt files, supporting both symmetric and asymmetric encryption.

- **Hardware Components:**
  - Raspberry Pi: The core hardware component that serves as an invisible intermediary between the user's computer and an external hard drive.
  - External Hard Drive: Used to store encrypted files securely.

## Usage

### Auto-Start

Upon connecting the Raspberry Pi to a computer, `MainGUI.py` will automatically start, providing a seamless and user-friendly experience.

### Encrypt Files

1. Choose to encrypt files for:
   - Group Sharing (Symmetric Encryption): Select a file, choose the encryption method, and the destination directory on the connected hard drive.
   - Individual Sharing (Asymmetric Encryption): Select a file, provide the recipient's public key, and choose the destination directory.

### Decrypt Files

1. Select the encrypted file and choose the decryption method:
   - Symmetric Encryption: Enter the encryption key and select the destination directory.
   - Asymmetric Encryption: Choose your private key file and the destination directory.

### Hardware Integration

- Connect the external hard drive to the Raspberry Pi.
- Configure the Raspberry Pi to recognize and mount the hard drive when connected.
- Implement logic in the scripts to handle file encryption, decryption, and data transfer to/from the hard drive.

## User Documentation

For detailed instructions on using the "Secure Data Encryption and Transfer Device," please refer to the user documentation provided with the project. It includes step-by-step guides, troubleshooting tips, and contact information for support.

## Testing and Feedback

We have extensively tested the SecureDataTransfer project to ensure the security and usability of the solution. However, user feedback is valuable for further improvements. Please feel free to provide feedback and report any issues in the project's repository.

## License

This project is licensed under the [MIT License](LICENSE).
