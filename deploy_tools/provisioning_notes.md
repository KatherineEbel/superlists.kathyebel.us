Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* venv + pip
* Git

eg, on Ubuntu 18.04

sudo apt update
sudo apt install nginx git python3-venv

## Nginx Virtual Host config

* see gunicorn-systemd.template.service
* sudo systemctl daemon-reload
* sudo systemctl restart <service_name>


Tutorial:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04

## Folder structure

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc

