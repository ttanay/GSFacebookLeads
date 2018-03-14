python3 -m venv src/env
pip3 install -r requirements.txt
sudo echo "alias fbscript='source src/env/bin/activate;python3 src/main.py;'" >> ~/.bashrc