pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "------------------------------------------------"
python3 utils/keyPairGenerator.py
# python3 mainGUI.py
