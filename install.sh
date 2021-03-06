#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
./src/manage.py collectstatic
./src/manage.py migrate
python3 setup.py develop
