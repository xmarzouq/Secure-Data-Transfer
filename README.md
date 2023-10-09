# Secure Data Transfer Device

**_Secure Data Transfer Device_** is a Raspberry Pi-based solution designed to provide secure and user-friendly data encryption and transfer capabilities. This project combines both hardware and software components to create a seamless and robust solution for protecting and sharing sensitive data.

## Table of Contents

- [Project Overview:](#project-overview)
  - [Software Components](#software-components)
  - [Hardware Components](#hardware-components)
- [Usage:](#usage)
  - [Auto-Start](#auto-start)
  - [Encrypting Files](#encrypting-files)
  - [Decrypting Files](#decrypting-files)
  - [Hardware Integration](#hardware-integration)
- [User Documentation](#user-documentation)
- [Testing and Feedback](#testing-and-feedback)
- [Dependencies](#dependencies)
- [License](#license)
- [Credits](#credits)
- [Badges](#badges)
- [How to Contribute](#how-to-contribute)

## Project Overview

The Secure Data Transfer Device consists of the following key components:

### Software Components:

1. **`MainGUI.py`:** This is the main graphical user interface (GUI) for the project. It offers users the choice to either encrypt or decrypt files.

2. **`Secure_Data_Transfer.py`:** This component manages the overall workflow, guiding users through the process of selecting files, encryption methods, and destination directories.

3. **`SymmetricEncryptAES.py`:** Responsible for handling symmetric encryption, particularly for group sharing scenarios, using the Advanced Encryption Standard (AES) algorithm.

4. **`AsymmetricRSAEncrypt.py`:** Manages asymmetric encryption for individual sharing, using RSA encryption with public keys to ensure secure data transfer.

5. **`Decrypt.py`:** Allows users to decrypt files, supporting both symmetric and asymmetric encryption methods.

### Hardware Components:

- **_Raspberry Pi:_** The core hardware component acts as an invisible intermediary between the user's computer and an external hard drive, enhancing data security.

- **_External Hard Drive:_** This hard drive is used to securely store encrypted files, ensuring that sensitive data remains protected even if the drive is lost or stolen.

## Usage

### Auto-Start

Upon connecting the Raspberry Pi to a computer, the `MainGUI.py` application will automatically launch, providing a seamless and user-friendly experience.

### Encrypting Files

Users can choose to encrypt files for:

- **Group Sharing (Symmetric Encryption):** Select a file, choose the encryption method, and specify the destination directory on the connected hard drive.

- **Individual Sharing (Asymmetric Encryption):** Select a file, provide the recipient's public key, and choose the destination directory.

### Decrypting Files

To decrypt files, follow these steps:

- **Symmetric Encryption:** Enter the encryption key and specify the destination directory.

- **Asymmetric Encryption:** Choose your private key file and the destination directory.

### Hardware Integration

1. Connect the external hard drive to the Raspberry Pi.

2. Configure the Raspberry Pi to recognize and automatically mount the hard drive when connected.

3. Implement logic within the scripts to handle file encryption, decryption, and data transfer to/from the hard drive.

## User Documentation

For comprehensive instructions on using the "Secure Data Transfer Device," please refer to the user documentation provided with the project. This documentation includes step-by-step guides, troubleshooting tips, and contact information for support.

## Testing and Feedback

The Secure Data Transfer Device project has undergone extensive testing to ensure both security and usability. However, user feedback is invaluable for further enhancements. Please feel free to provide feedback and report any issues in the project's repository.

## Dependencies

This project relies on the following dependencies:

- [Python](https://www.python.org/): The primary programming language used for scripting and development.
- [PyQt5](https://pypi.org/project/PyQt5/): A Python binding for the Qt application framework, used for creating the graphical user interface (GUI).
- [Crypto](https://pypi.org/project/pycryptodome/): A cryptographic library for Python, providing support for encryption and decryption operations.
- [Raspberry Pi OS](https://www.raspberrypi.org/software/): The operating system for the Raspberry Pi, which serves as the core hardware component.

Please ensure that these dependencies are installed and configured correctly to run the Secure Data Transfer Device.

## License

This project is open-source and released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) - check the [License](LICENSE) file for more details

## Credits

This project was developed by **_Marzouq_**, and it benefited from the valuable insights and contributions of the open-source community. We extend our gratitude to all those who have supported this project.

## Badges

## How to Contribute

If you would like to contribute to this project, please review our [Contribution Guidelines](CONTRIBUTING.md) for detailed information on creating issues, suggesting new features, and submitting pull requests.
