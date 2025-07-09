#!/bin/bash

path=$(pwd)
python_bin = "/usr/local/Cellar/python@3.13/3.13.5/bin/python3"
pip_bin = "/usr/local/Cellar/python@3.13/3.13.5/bin/pip3"

cp "${path}/env.example" "${path}/code/.env"
cp "${path}/env.example" "${path}/frontend/.env"
cd code
curl -sSL https://install.python-poetry.org | $python_bin -
poetry env use $python_bin
poetry install
$pip_bin install . --break-system-packages
$python_bin manage.py migrate
cd ../frontend
npm install --force
npm run build-prod
cd ..
ln -s "${path}/frontend/dist/glitchtip-frontend/" "${path}/code/dist"
cd code
$python_bin manage.py collectstatic

# start server
# python3 manage.py runserver

# restart pm2 service
# pm2 restart glitctip
# pm2 restart glitctip-celery
# ln -s "/Applications/MAMP/htdocs/glitchtip-repo/frontend/dist/glitchtip-frontend/" "/Applications/MAMP/htdocs/glitchtip-repo/code/dist/"