sudo pip install --upgrade pip
sudo pip install Flask
sudo pip install Flask-MySQLdb

sudo cp ./stoplicht.service /etc/systemd/system/stoplicht.service

chmod +x ./main.py

#enable the system file
sudo systemctl start stoplicht.service
sudo systemctl enable stoplicht.service
sudo systemctl daemon-reload
sudo systemctl start stoplicht.service

