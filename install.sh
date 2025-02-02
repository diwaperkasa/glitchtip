#!/bin/bash

path=$(pwd)

cp "${path}/env.example" "${path}/code/.env"
cp "${path}/env.example" "${path}/frontend/.env"
cd code
curl -sSL https://install.python-poetry.org | python3 -
poetry install
/Users/user/.pyenv/shims/pip3.10 install .
/Users/user/.pyenv/shims/python3.10 manage.py migrate
cd ../frontend
npm install --force
npm run build-prod
cd ..
ln -s "${path}/frontend/dist/glitchtip-frontend/" "${path}/code/dist"
cd code
/Users/user/.pyenv/shims/python3 manage.py collectstatic

# start server
# python3 manage.py runserver

# restart pm2 service
# pm2 restart glitctip
# pm2 restart glitctip-celery