#!/bin/bash
cd /code
python manage.py makemigrations
python manage.py migrate
python manage.py populate_database
python -u manage.py runserver 0.0.0.0:8000