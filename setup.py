from setuptools import setup, find_packages

setup(
    name='secureDataTransfer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project requires
        'pycryptodome>=3.11.0',
        'PyQt5>=5.15.0',
    ],
    entry_points={
        'console_scripts': [
            'secureDataTransfer = secureDataTransfer.mainGUI:main',
        ],
    },
)
