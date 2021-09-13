#!/bin/bash

# Install packages for dev, please comment out for prod
pip3 install -r requirements/dev.txt

# Set setting env for dev, please switch "dev" to "prod" for prod
export DJANGO_SETTINGS_MODULE=config.settings.dev

# Prepare database
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@example.com', 'adminpass');"

# Collect Staticfiles
python3 manage.py collectstatic --noinput

# Launch server
python3 manage.py runserver 0.0.0.0:8000