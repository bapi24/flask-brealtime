#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install apache2
sudo apt-get -y install libapache2-mod-wsgi
sudo apt-get -y install python-pip
sudo pip install flask
sudo apt-get -y install git
git clone https://github.com/bapi24/flask-brealtime.git
sudo ln -sT ~/flask-brealtime /var/www/html/flask-brealtime
