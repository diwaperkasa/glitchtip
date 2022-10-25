#!/bin/bash

python -u /Applications/MAMP/htdocs/glitchtip/code/manage.py runserver

pm2 start --name glitchtip --interpreter python /Applications/MAMP/htdocs/glitchtip/code/manage.py -- runserver