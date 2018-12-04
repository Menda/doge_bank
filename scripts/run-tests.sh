#!/bin/bash

pip install -r requirements/ci.txt

cat .flake8
flake8 .

python manage.py test -v 2
