python3 -m venv src/env
source src/env/bin/activate
pip3 install -r requirements.txt
deactivate
sudo echo "alias fbscript='source src/env/bin/activate;python3 src/main.py;'" >> ~/.bashrc
exit