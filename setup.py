from setuptools import setup, find_packages

setup(
    name="secureDataTransfer",
    version="0.1.0",
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
