#!/bin/bash
# Setup up the venv, runs the script, copies file to /var/www/html

source ~/api_permission_bot/venv/bin/activate
python3 ~/api_permission_bot/api_permission_bot.py
cp ~/api_permission_bot/api_permission.html /var/www/html/index.html
