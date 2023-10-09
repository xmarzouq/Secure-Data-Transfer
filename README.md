<!-- Title Section -->
<h1 align="center">Secure Data Transfer Device 🛡️</h1>

<p align="center">
  <strong>A Raspberry Pi-based solution for secure and user-friendly data encryption and transfer.</strong>
</p>

<h2 align="left">Content Table</h2>


  - [Project Overview](#project-overview)
    - [Software Components](#software-components)
    - [Hardware Components](#hardware-components)
  - [Usage](#usage)
    - [Auto-Start](#auto-start)
    - [Encrypting Files](#encrypting-files)
    - [Decrypting Files](#decrypting-files)
    - [Hardware Integration](#hardware-integration)
  - [User Documentation](#user-documentation)
  - [Testing and Feedback](#testing-and-feedback)
  - [License](#license)
  - [Credits](#credits)
  - [Badges](#badges)
  - [How to Contribute](#how-to-contribute)

<!-- Project Description -->
<h2 align="center">Project Overview</h2>

<p align="center">
  <em>Protecting Sensitive Data Made Simple.</em>
</p>

The **Secure Data Transfer Device** seamlessly combines hardware and software components to create a robust solution for safeguarding and sharing sensitive information.

---
<!-- Components Section -->
<h2 align="center">📦 Software & Hardware Components</h2>

<p align="center">
  <em>Explore the Core Components</strong>
</p>

<p align="center">
  <a href="#software-components">Software Components</a> |
  <a href="#hardware-components">Hardware Components</a>
</p>

<!-- Software Components Section -->
<h4 align="left" id="software-components">Software Components</h4>

- **`MainGUI.py`**: The intuitive graphical interface, allowing you to encrypt or decrypt files effortlessly.

- **`Secure_Data_Transfer.py`**: The workflow manager, guiding you through file selection, encryption, and destination directory.

- **`SymmetricEncryptAES.py`**: Handles symmetric encryption, perfect for secure group sharing using the AES algorithm.

- **`AsymmetricRSAEncrypt.py`**: Employs RSA encryption with public keys for individual sharing, ensuring data security.

- **`Decrypt.py`**: Facilitates file decryption, supporting both symmetric and asymmetric encryption.

<!-- Hardware Components Section -->
<h4 align="left" id="hardware-components">Hardware Components</h4>

- **_Raspberry Pi:_** The invisible guardian between your computer and an external hard drive, fortifying data security.

- **_External Hard Drive:_** A secure vault for your encrypted files, ensuring data remains protected, even if the drive is misplaced.

---
<!-- Usage Section -->
<h2 align="center">Usage</h2>

<p align="center">
  <em>Your Data, Your Control.</em>
</p>

<p align="center">
  <a href="#auto-start">Auto-Start</a> |
  <a href="#encrypting-files">Encrypting Files</a> |
  <a href="#decrypting-files">Decrypting Files</a> |
  <a href="#hardware-integration">Hardware Integration</a>
</p>

### Auto-Start

Connect the Raspberry Pi to your computer, and the `MainGUI.py` application will auto-launch, offering a seamless user experience.

### Encrypting Files

Secure your files for:

- **Group Sharing (Symmetric Encryption):** Select a file, pick the encryption method, and specify the destination directory on the connected hard drive.

- **Individual Sharing (Asymmetric Encryption):** Select a file, provide the recipient's public key, and choose the destination directory.

### Decrypting Files

To decrypt files:

- **Symmetric Encryption:** Enter the encryption key and choose the destination directory.

- **Asymmetric Encryption:** Pick your private key file and the destination directory.

---
<!-- Hardware Integration Section -->
<h2 align="center">Hardware Integration</h2>

<p align="center">
  <em>Seamless, Yet Robust.</em>
</p>

1. Connect the external hard drive to the Raspberry Pi.

2. Power up the Raspberry Pi to recognize and auto-mount the hard drive upon connection.

3. Connect the Raspberry Pi to the computer  handle file encryption, decryption, and data transfer to/from the hard drive.

<!-- User Documentation Section -->
<h2 align="center">User Documentation</h2>

<p align="center">
  <em>Guides, Tips, and Support.</em>
</p>

For comprehensive instructions on using the "Secure Data Transfer Device," please refer to the user documentation provided with the project. This documentation includes step-by-step guides, troubleshooting tips, and contact information for support.

<!-- Testing and Feedback Section -->
<h2 align="center">Testing and Feedback</h2>

<p align="center">
  <em>We Value Your Input.</em>
</p>

The Secure Data Transfer Device project has undergone extensive testing to ensure both security and usability. However, user feedback is invaluable for further enhancements. Please feel free to provide feedback and report any issues in the project's repository.

<!-- Dependencies Section -->
<h2 align="center">Dependencies</h2>

<p align="center">
  <em>The Building Blocks.</em>
</p>

This project relies on the following dependencies:

- [Python](https://www.python.org/): The primary programming language used for scripting and development.

- [PyQt5](https://pypi.org/project/PyQt5/): A Python binding for the Qt application framework, used for creating the graphical user interface (GUI).

- [Crypto](https://pypi.org/project/pycryptodome/): A cryptographic library for Python, providing support for encryption and decryption operations.

- [Raspberry Pi OS](https://www.raspberrypi.org/software/): The operating system for the Raspberry Pi, which serves as the core hardware component.

Please ensure that these dependencies are installed and configured correctly to run the Secure Data Transfer Device.

<!-- License Section -->
<h2 align="center">License</h2>

<p align="center">
  <em>Open Source and Free to Use.</em>
</p>

This project is open-source and released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) - check the [License](LICENSE) file for more details

<!-- Credits Section -->
<h2 align="center">Credits</h2>

<p align="center">
  <em>Thanks to Our Contributors.</em>
</p>

This project was developed by a dedicated senior students group, and it benefited from the valuable insights and contributions of the university researchers. We extend our gratitude to all those who have supported this project.

<!-- Badges and Contributions Section -->
<h2 align="center">Contributions</h2>

<p align="center">
  <em>Join Us and Make a Difference.</em>
</p>

If you would like to contribute to this project, please review our [Contribution Guidelines](CONTRIBUTING.md) for detailed information on creating issues, suggesting new features, and submitting pull requests.
