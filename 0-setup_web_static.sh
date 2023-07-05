#!/usr/bin/env bash
# Set up server file system for deployment

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# configure file system
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html><head></head><body>Holberton School<body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# set permissions
sudo chown -R ubuntu:ubuntu /data/
#create a copy of current default before modifying
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default_copy
# configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
# Test config
sudo nginx -t
# restart web server
sudo service nginx restart
