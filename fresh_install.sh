#!/bin/bash

rm -rf code
rm -rf frontend

glitchtip_version=v5.0.5

git clone https://gitlab.com/glitchtip/glitchtip-backend.git code
cd code
git checkout "${glitchtip_version}"
cd ..
git clone https://gitlab.com/glitchtip/glitchtip-frontend.git frontend
cd frontend
git checkout "${glitchtip_version}"
cd ..

sh ./install.sh
