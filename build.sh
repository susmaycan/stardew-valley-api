#!/usr/bin/env bash

set -o errexit  # exit on error

apt-get install python3-dev

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
