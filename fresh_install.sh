#!/bin/bash

rm -rf code
rm -rf frontend

git clone https://gitlab.com/glitchtip/glitchtip-backend.git code
git clone https://gitlab.com/glitchtip/glitchtip-frontend.git frontend

sh ./install.sh