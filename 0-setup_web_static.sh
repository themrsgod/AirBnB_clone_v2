#!/usr/bin/env bash
# Setting up server file system for deployment

# install nginx if not done
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# configuring file system
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html><head></head><body>Holberton School<body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# setting up permissions
sudo chown -R ubuntu:ubuntu /data/
#creating a copy of current default before modifying
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default_copy
# Configuring nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
# Testing config
sudo nginx -t
# restarting the web server
sudo service nginx restart
