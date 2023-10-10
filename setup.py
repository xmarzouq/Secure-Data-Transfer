from setuptools import setup, find_packages

setup(
    name="secureDataTransfer",
    version="0.1.2",
    description="The 'Secure Data Transfer'  seamlessly is a robust solution for safeguarding and sharing sensitive information.",
    packages=find_packages(),
    install_requires=[
        "pycryptodome>=3.10.1",
        "pyqt5>=5.15.4"
    ],
    entry_points={
        "console_scripts": [
            "secure-data-transfer = secureDataTransfer.mainGUI:main"
        ]
    },
)
