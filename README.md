# Secure Data Transfer Device

## Project Overview

The "Secure Data Transfer Device" is designed to provide a secure and user-friendly solution for encrypting, transferring, and decrypting data while maintaining data privacy and security. This project utilizes a Raspberry Pi as a core hardware component, acting as an invisible intermediary between the user's computer and an external hard drive. It ensures data security and enables users to interact seamlessly with the device.

## Table of Contents

1. [Software Components](#software-components)
2. [Hardware Components](#hardware-components)
3. [User Interaction](#user-interaction)
4. [User Documentation](#user-documentation)
5. [Testing and Feedback](#testing-and-feedback)

## Software Components

### MainGUI.py

- **Purpose:** The main graphical user interface (GUI) serves as the entry point for the user.
- **Functionality:**
  - Allows the user to choose between encrypting and decrypting files.
  - Initiates the appropriate encryption or decryption process based on user selection.
  - Hides the presence of the Raspberry Pi, ensuring a seamless user experience.

### Secure_Data_Transfer.py

- **Purpose:** Acts as a central control script that manages data encryption, transfer, and decryption.
- **Functionality:**
  - Coordinates the selection of encryption methods (symmetric or asymmetric) based on user input.
  - Ensures that data is securely encrypted before transferring it to an external hard drive.
  - Interacts with SymmetricEncryptAES.py, AsymmetricRSAEncrypt.py, and Decrypt.py as needed.

### SymmetricEncryptAES.py

- **Purpose:** Handles symmetric encryption for group-based file sharing.
- **Functionality:**
  - Prompts the user to choose a file for encryption.
  - Accepts an encryption key from the user.
  - Encrypts the file using the AES algorithm.
  - Allows the user to select a directory on an external hard drive for storing the encrypted file.

### AsymmetricRSAEncrypt.py

- **Purpose:** Manages asymmetric encryption for individual file sharing.
- **Functionality:**
  - Prompts the user to select a recipient's public key file.
  - Encrypts the selected file using the recipient's public key.
  - Allows the user to choose a directory on an external hard drive for storing the encrypted file.

### Decrypt.py

- **Purpose:** Handles file decryption based on the selected encryption method.
- **Functionality:**
  - Determines the encryption method used for the encrypted file (symmetric or asymmetric) based on user input.
  - Decrypts the file using the appropriate decryption key or private key.
  - Allows the user to choose a directory for saving the decrypted file.

## Hardware Components

### Raspberry Pi

- **Role:** The core hardware component that acts as an invisible intermediary.
- **Functionality:**
  - Recognizes the external hard drive.
  - Executes the software scripts.
  - Ensures data encryption before writing to the hard drive.
  - Provides an additional layer of security for data storage and transfer.

### External Hard Drive

- **Role:** The storage medium for encrypted files.
- **Functionality:**
  - Connects to the Raspberry Pi.
  - Receives encrypted files for storage.
  - Safely stores encrypted data.

## User Interaction

**Encryption:**

1. User inserts the Raspberry Pi into their computer.
2. MainGUI.py is automatically initiated, displaying the GUI.
3. User selects the "Encrypt" option.
4. Secure_Data_Transfer.py coordinates the process.
5. User decides whether to share with a group (Symmetric Encryption) or an individual (Asymmetric Encryption).

**Decryption:**

1. User inserts the Raspberry Pi into their computer.
2. MainGUI.py is automatically initiated, displaying the GUI.
3. User selects the "Decrypt" option.
4. Secure_Data_Transfer.py coordinates the process.
5. User specifies the encryption method (Symmetric or Asymmetric) used for the encrypted file.
6. User provides the decryption key or private key, depending on the method chosen.

**Security and Transparency:**

- The Raspberry Pi remains hidden from the user's view during interaction.
- All encryption and decryption processes are transparent to the user through the GUI.
- Data remains secure even if the external hard drive is lost or stolen.

## User Documentation

**Detailed User Guide:**

- Explains how to use the "Secure Data Transfer Device."
- Provides step-by-step instructions on inserting the Raspberry Pi, interacting with the GUI, and securely ejecting the device.
- Includes troubleshooting steps and support contact information.

## Testing and Feedback

**Testing:**

- Thoroughly tests the entire workflow, including encryption, decryption, and data transfer.
- Ensures that security measures work as intended.

**User Feedback:**

- Gathers user feedback to identify areas for improvement.
- Makes necessary adjustments and refinements to the software and hardware components based on testing and user feedback.

## License

This project is licensed under the [MIT LICENSE] - see the [LICENSE.md](LICENSE) file for details.
