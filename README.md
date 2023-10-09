<!-- PROJECT SHIELDS -->
<!--
*** Thanks for checking out the SecureDataTransfer project! If you have any suggestions
*** or feedback, please feel free to contribute.
*** Don't forget to give the project a star!
*** Thanks for your support!
-->

<!-- PROJECT LOGO -->
<div align="center">
  <h1>SecureDataTransfer</h1>
  <p>An innovative Raspberry Pi-based solution for secure and user-friendly data encryption and transfer.</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#auto-start">Auto-Start</a></li>
        <li><a href="#encrypt-files">Encrypt Files</a></li>
        <li><a href="#decrypt-files">Decrypt Files</a></li>
        <li><a href="#hardware-integration">Hardware Integration</a></li>
      </ul>
    </li>
    <li><a href="#user-documentation">User Documentation</a></li>
    <li><a href="#testing-and-feedback">Testing and Feedback</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Screenshot](product-screenshot-link)](product-screenshot-link)

SecureDataTransfer is a Raspberry Pi-based solution designed to enhance data security and privacy. It provides a seamless user experience while ensuring that sensitive data remains protected during storage and transfer.

### Built With

- [Python](https://www.python.org/)
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
- [Crypto](https://pypi.org/project/pycryptodome/)

<!-- GETTING STARTED -->
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

<!-- USER DOCUMENTATION -->
## User Documentation

For detailed instructions on using the "Secure Data Encryption and Transfer Device," please refer to the user documentation provided with the project. It includes step-by-step guides, troubleshooting tips, and contact information for support.

<!-- TESTING AND FEEDBACK -->
## Testing and Feedback

We have extensively tested the SecureDataTransfer project to ensure the security and usability of the solution. However, user feedback is valuable for further improvements. Please feel free to provide feedback and report any issues in the project's repository.

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
- [Malven's Grid Cheatsheet](https://grid.malven.co/)
- [Img Shields](https://shields.io)
- [GitHub Pages](https://pages.github.com)
- [Font Awesome](https://fontawesome.com)
- [React Icons](https://react-icons.github.io/react-icons/search)
