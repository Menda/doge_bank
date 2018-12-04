#!/bin/bash

# DEV ONLY, DO NOT USE IN PRODUCTION

echo $(date -u) "- Migrating"
python manage.py migrate

echo $(date -u) "- Creating admin user"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

echo $(date -u) "- Running the server"
python manage.py runserver 0.0.0.0:8000
